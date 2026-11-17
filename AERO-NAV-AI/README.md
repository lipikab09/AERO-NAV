AERO-NAV AI: Advanced Multi-Modal Sensor Fusion & Neural SLAM System for GPS-Denied Autonomous Drone Navigation

A research-oriented, production-engineered multi-modal sensor fusion and Neural SLAM system designed for robust autonomous drone navigation in GPS-denied environments (e.g., underground tunnels, indoor facilities, urban canyons, and GNSS-jammed airspace).

🚀 System Overview & Architecture

AERO-NAV AI couples high-frequency IMU pre-integration, solid-state LiDAR point clouds, and stereo vision with a deep panoptic perception branch and a factor-graph optimization backend. This achieves centimeter-level localization accuracy under extreme visual degradation, sensor dropouts, and complete GPS denial.

[ Asynchronous Sensors: IMU / LiDAR / Stereo ] 
                    │
                    ▼
        [ Ingestion & Validity Masks ]
                    │
                    ▼
     [ Panoptic Segmentation & Depth ] ◄─── [ Epistemic & Aleatoric Uncertainty Layer ]
                    │
                    ▼
       [ Neural VIO & EKF State Estimator ]
                    │
                    ▼
       [ FastAPI Backend & 3D WebGL Command Center ]


📂 Repository Contents & Codebase Structure

AERO-NAV-AI/
├── config/
│   └── default_config.yaml         # System hyperparameters, sensor rates, and confidence thresholds
├── src/
│   ├── ingestion/
│   │   └── pipeline.py             # Asynchronous sensor streams & explicit validity mask handlers
│   ├── perception/
│   │   └── panoptic.py             # Real-time panoptic segmentation & traversability costmap generator
│   ├── slam/
│   │   └── vio_gtsam.py            # Deep Visual-Inertial Odometry (VIO) & EKF kinematic backend
│   ├── safety/
│   │   └── uncertainty.py          # Monte Carlo Dropout epistemic uncertainty & emergency hover supervisor
│   └── backend/
│       └── app.py                  # FastAPI server with WebSocket real-time telemetry streaming
├── dashboard/
│   └── app.py                      # Streamlit 3D interactive command center and flight visualization
├── tests/
│   └── test_safety.py              # Pytest unit tests for uncertainty and perception modules
├── Dockerfile                      # Production container build definition
├── docker-compose.yml              # Multi-container orchestration (Backend + Dashboard)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation


🛠️ Installation & Getting Started (VS Code PowerShell)

1. Clone & Set Up Environment

git clone https://github.com/lipikab09/AERO-NAV-AI.git
cd AERO-NAV-AI
python -m venv venv
.\venv\Scripts\Activate.ps1


2. Install Dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt


3. Run Unit Tests

Verify module integration and safety interlocks:

$env:PYTHONPATH="."; python -m pytest tests/ -v


🚀 Running the System

Terminal 1: Launch FastAPI Telemetry Backend

python -m uvicorn src.backend.app:app --host 0.0.0.0 --port 8000 --reload


Terminal 2: Launch 3D Command Center Dashboard

Open a new PowerShell tab:

.\venv\Scripts\Activate.ps1
streamlit run dashboard/app.py


🐳 Docker Deployment

To run the complete system containerized:

docker-compose up --build


📄 License

Distributed under the MIT License. See LICENSE for more information.