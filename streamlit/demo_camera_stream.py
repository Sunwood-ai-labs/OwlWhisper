import streamlit as st
import cv2
import numpy as np
import requests
from threading import Thread
from streamlit.server.server import Server

class VideoStream:
    def __init__(self, url):
        self.url = url
        self.byte_buffer = bytes()
        self.frame = None
        self.running = True

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        with requests.get(self.url, stream=True) as response:
            for chunk in response.iter_content(chunk_size=1024):
                if not self.running:
                    break
                self.byte_buffer += chunk
                a = self.byte_buffer.find(b'\xff\xd8')
                b = self.byte_buffer.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = self.byte_buffer[a:b+2]
                    self.byte_buffer = self.byte_buffer[b+2:]
                    self.frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

    def read(self):
        return self.frame

    def stop(self):
        self.running = False

def main():
    st.title("Real-time Video Stream")
    stream_url = 'http://host.docker.internal:8001/camera'
    video_stream = VideoStream(stream_url).start()

    placeholder = st.empty()

    while True:
        frame = video_stream.read()
        if frame is not None:
            placeholder.image(frame, channels="BGR")
        Server.get_current()._loop.call_later(0.1, st.experimental_rerun)

    video_stream.stop()

if __name__ == "__main__":
    main()
