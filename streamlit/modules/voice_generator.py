import requests
import os

STYLE_BERT_VITS2_API_URL = os.getenv("STYLE_BERT_VITS2_API_URL")

def generate_voice(text):
    params = {
        "text": text,
        "encoding": "utf-8",
        "model_id": 0,
        "speaker_id": 0,
        "sdp_ratio": 0.2,
        "noise": 0.6,
        "noisew": 0.8,
        "length": 1,
        "language": "JP",
        "auto_split": True,
        "split_interval": 0.5,
        "assist_text": "",
        "assist_text_weight": 1,
        "style": "Neutral",
        "style_weight": 5
    }
    response = requests.get(STYLE_BERT_VITS2_API_URL, params=params)
    if response.status_code == 200:
        return response.content
    else:
        print("音声生成エラー:", response.status_code)
        return None