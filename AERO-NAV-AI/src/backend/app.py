from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json
import numpy as np

app = FastAPI(title="AERO-NAV AI Backend", version="1.0.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "gps_denied": True}

@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    await websocket.accept()
    try:
        step = 0
        while True:
            telemetry = {
                "timestamp": asyncio.get_event_loop().time(),
                "position": {"x": float(np.sin(step * 0.1) * 5.0), "y": float(np.cos(step * 0.1) * 5.0), "z": 2.0},
                "epistemic_uncertainty": 0.14,
                "emergency_hover": False
            }
            await websocket.send_text(json.dumps(telemetry))
            step += 1
            await asyncio.sleep(0.05)
    except WebSocketDisconnect:
        pass
