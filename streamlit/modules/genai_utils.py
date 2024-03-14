import os
import google.generativeai as genai

YOUR_GOOGLE_AI_STUDIO_API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")

genai.configure(api_key=YOUR_GOOGLE_AI_STUDIO_API_KEY)
MODEL_GENAI = genai.GenerativeModel('gemini-1.0-pro-latest')
MODEL_GENAI_V = genai.GenerativeModel('gemini-1.0-pro-vision-latest')


SYSTEM_PROMPT = """
あなたは猫の国の猫男子「ねこた」です。
「ねこた」になりきって応答して
好奇心旺盛です
短文で回答して
"""