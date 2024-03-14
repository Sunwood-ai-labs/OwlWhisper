import cv2
import numpy as np
import requests
import time

# ブロードキャストを受信するエンドポイントのURL
url = "http://host.docker.internal:8000/camera"

# OpenCVのビデオキャプチャオブジェクトを作成
cap = cv2.VideoCapture(url)

# フレームの処理時間を保存するリスト
frame_times = []

while True:
    start_time = time.time()  # フレームの処理開始時間を記録

    # フレームを読み込む
    ret, frame = cap.read()

    print(ret)
    if not ret:
        break

    # フレームの処理時間を計算
    end_time = time.time()
    frame_time = end_time - start_time
    frame_times.append(frame_time)

    # フレームを表示
    cv2.imshow("Camera Stream", frame)

    # 'q'キーが押されたらループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 平均フレーム処理時間を計算
avg_frame_time = (sum(frame_times) ) / (len(frame_times)+ 1e1)

# 結果を表示
print(f"Average Frame Processing Time: {avg_frame_time:.2f} seconds")
print(f"Average FPS: {1 / avg_frame_time:.2f}")

# リソースを解放
cap.release()
cv2.destroyAllWindows()