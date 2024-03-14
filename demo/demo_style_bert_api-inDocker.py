import requests
import os
import time

# APIのベースURL
url = "http://style-bert-vits2-api:5000/voice"

# クエリパラメータ
params = {
    "text": "こんにちは、今日の気分はどうですか？",
    "encoding": "utf-8",  # 必要に応じて指定
    "model_id": 0,
    "speaker_id": 0,
    "sdp_ratio": 0.2,
    "noise": 0.6,
    "noisew": 0.8,
    "length": 1,
    "language": "JP",
    "auto_split": True,
    "split_interval": 0.5,
    "assist_text": "",  # この例では空ですが、必要に応じて指定
    "assist_text_weight": 1,
    "style": "Neutral",
    "style_weight": 5
}

# 出力フォルダのパス
output_folder = "output"

# フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 音声ファイルの保存パス
output_path = os.path.join(output_folder, "output.wav")

# リクエスト開始時間を記録
start_time = time.time()

# リクエストの送信とレスポンスの確認
response = requests.get(url, params=params)  # `url` と `params` は前の手順と同じ

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
    print("エラーが発生しました。ステータスコード:", response.status_code)


"""
C:\Prj\OwlWhisper\demo>python demo_style_bert_api.py
音声ファイルを 'output\output.wav' に保存しました。
リクエストにかかった時間: 0.80秒
"""