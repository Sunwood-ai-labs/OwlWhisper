# modules/video_transformer.py
import cv2
import time
import os
import streamlit as st
from streamlit_webrtc import VideoTransformerBase

# modules/video_transformer.py
import cv2
import time
import os
import streamlit as st
from streamlit_webrtc import VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.url = os.getenv("CAMERA_URL")
        self.cap = cv2.VideoCapture(self.url)
        self.frame_times = []
        print(f"CAMERA_URL:{self.url}")

    def transform(self, frame):
        start_time = time.time()  # フレームの処理開始時間を記録

        img = frame.to_ndarray(format="bgr24")

        # フレームの処理時間を計算
        end_time = time.time()
        frame_time = end_time - start_time
        self.frame_times.append(frame_time)

        return img

    def teardown(self):
        # 平均フレーム処理時間を計算
        avg_frame_time = (sum(self.frame_times)) / (len(self.frame_times) + 1e-10)

        # 結果を表示
        st.write(f"Average Frame Processing Time: {avg_frame_time:.2f} seconds")
        st.write(f"Average FPS: {1 / avg_frame_time:.2f}")

        self.cap.release()