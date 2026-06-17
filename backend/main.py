from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Tauri-Python Audio Engine Bridge", version="1.0.0")

class AudioPayload(BaseModel):
    batch_id: str
    input_tracks: list[str]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "cuda_available": True}

@app.post("/pipeline/process")
async def trigger_pipeline(payload: AudioPayload):
    return {"success": True, "batch_id": payload.batch_id, "status": "queued"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
