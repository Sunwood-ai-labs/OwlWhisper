call conda activate yva
uvicorn YlvaVisionAPI.api.camera_server_broadcast:app --reload  --host=0.0.0.0 --port=8100