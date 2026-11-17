import asyncio
import numpy as np
from typing import Dict, Any, Optional, AsyncGenerator

class SensorIngestionPipeline:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.tolerance_sec = config.get("ingestion", {}).get("time_sync_tolerance_ms", 15.0) / 1000.0

    async def ingest_stream(self, raw_sensor_stream: AsyncGenerator[Dict[str, Any], None]) -> AsyncGenerator[Dict[str, Any], None]:
        async for packet in raw_sensor_stream:
            t_cam = packet.get("timestamp_camera", 0.0)
            t_imu = packet.get("timestamp_imu", 0.0)
            t_lidar = packet.get("timestamp_lidar", 0.0)

            max_t = max(t_cam, t_imu, t_lidar)
            min_t = min(t_cam, t_imu, t_lidar)
            packet["sync_valid"] = (max_t - min_t) <= self.tolerance_sec

            packet["validity_mask"] = {
                "camera": packet.get("camera_frame") is not None,
                "imu": packet.get("imu_data") is not None,
                "lidar": packet.get("lidar_cloud") is not None
            }
            yield packet
