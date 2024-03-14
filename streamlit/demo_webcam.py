import streamlit as st
from streamlit_webrtc import webrtc_streamer
from modules.video_transformer import VideoTransformer

st.title('Streamlit App Test')
st.write('Hello world')

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)