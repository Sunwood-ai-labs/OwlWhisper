import streamlit as st
from audio_recorder_streamlit import audio_recorder
import requests
import base64
import time
from PIL import Image
import cv2
import io
import os

# モジュールのインポート（音声生成、GENAIユーティリティ等）
from modules.voice_generator import generate_voice
from modules.genai_utils import genai, MODEL_GENAI, SYSTEM_PROMPT, MODEL_GENAI_V

# カメラURLとビデオキャプチャの設定
CAMERA_URL = os.getenv("CAMERA_URL")
cap = cv2.VideoCapture(CAMERA_URL)

FAST_WISPER_API_URL = os.getenv("FAST_WISPER_API_URL")

# Streamlitアプリケーションのタイトル設定
st.title("Owl Wisper DEMO")

# サイドバーの設定
with st.sidebar:
    st.markdown("""
        <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/OwlWhisper/main/docs/OwlWhisper.png" height=400px align="left"/>
        """, unsafe_allow_html=True)
    
    # 音声録音ウィジェット
    audio_bytes = audio_recorder(pause_threshold=30)
    ret, _ = cap.read()
    if(ret):
        st.success("CAM OK")
    else:
        st.warning("CAM NG")
    input_vision = st.checkbox('画像を入力', value=True)
    img_scale = st.slider('画像のスケール', min_value=1, max_value=10, value=3, step=1)

# メッセージの保存用
if "messages" not in st.session_state:
    st.session_state.messages = []

# 音声データが存在する場合、Wisper APIに送信してテキストに変換
if audio_bytes is not None:
    
    files = {"audio_file": ("audio.wav", audio_bytes, "audio/wav")}
    response = requests.post(FAST_WISPER_API_URL, files=files)
    
    if response.status_code == 200:
        data = response.json()
        transcribed_text = "".join(segment['text'] for segment in data["transcribed_text"])
        prompt = transcribed_text
    else:
        st.error("音声をテキストに変換する際にエラーが発生しました。")
else:
    prompt = st.text_input("What is up?")

# プロンプト（テキスト入力または音声入力からのテキスト）が存在する場合
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 画像データの取得と処理
    ret, image_data = cap.read()
    if ret and input_vision:
        height, width = image_data.shape[:2]
        new_height, new_width = height // img_scale, width // img_scale
        image_data = cv2.resize(image_data, (new_width, new_height))
        image_data_rgb = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image_data_rgb)
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)
        img = Image.open(buffer)
        # GENAIモデルを使用して画像付きでレスポンス生成
        assistant_message = MODEL_GENAI_V.generate_content([prompt, img])
    else:
        # GENAIモデルを使用してテキストのみでレスポンス生成
        assistant_message = MODEL_GENAI.generate_content(prompt)
    
    # アシスタントメッセージの表示
    if ret and input_vision:
        st.session_state.messages.append({"role": "assistant", "content": assistant_message.text, "image": image_data})
    else:
        st.session_state.messages.append({"role": "assistant", "content": assistant_message.text})
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "image" in message:
                st.image(message["image"], use_column_width=True)
    
    # 音声応答の生成と再生
    voice_data = generate_voice(assistant_message.text)
    if voice_data:
        audio_str = "data:audio/ogg;base64,%s" % (base64.b64encode(voice_data).decode())
        audio_html = f"""
            <audio autoplay=True>
                <source src="{audio_str}" type="audio/ogg" autoplay=True>
                Your browser does not support the audio element.
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
