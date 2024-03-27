FROM python:3.11

WORKDIR /app

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev

RUN pip install --upgrade pip  \
                streamlit \
                audio-recorder-streamlit \
                fastapi uvicorn python-multipart \
                google-generativeai 
RUN pip install opencv-python streamlit-webrtc
RUN pip install audio-recorder-streamlit pydub