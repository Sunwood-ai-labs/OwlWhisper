import requests
import os
import time

# APIのベースURL
url = "http://localhost:5000/voice"

# audio/thinkingフォルダのパス
thinking_folder = "audio/thinking"

# audio/thinkingフォルダ内のtxtファイルを取得
txt_files = [file for file in os.listdir(thinking_folder) if file.endswith(".txt")]

# txtファイルごとに処理
for txt_file in txt_files:
    # txtファイルの名前（拡張子なし）
    word_list_name = os.path.splitext(txt_file)[0]

    # テキストファイルのパス
    text_file_path = os.path.join(thinking_folder, txt_file)

    # 出力フォルダのパス
    output_folder = os.path.join(thinking_folder, word_list_name)

    # フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # テキストファイルを読み込み、改行で区切る
    with open(text_file_path, "r", encoding="utf-8") as file:
        sentences = file.read().splitlines()

    # 文章ごとに音声を生成
    for index, sentence in enumerate(sentences):
        # クエリパラメータ
        params = {
            "text": sentence,
            "encoding": "utf-8",
            "model_id": 1,
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

        # 音声ファイルの保存パス（数値のファイル名、0埋めあり）
        output_path = os.path.join(output_folder, f"{index:04d}.wav")

        # リクエスト開始時間を記録
        start_time = time.time()

        # リクエストの送信とレスポンスの確認
        response = requests.get(url, params=params)

        # リクエスト終了時間を記録
        end_time = time.time()

        # リクエストにかかった時間を計算
        request_time = end_time - start_time

        if response.status_code == 200:
            # レスポンスから音声データを取得し、ファイルに保存
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"音声ファイルを '{output_path}' に保存しました。")
            print(f"リクエストにかかった時間: {request_time:.2f}秒")
        else:
            print(f"エラーが発生しました。ステータスコード: {response.status_code}")