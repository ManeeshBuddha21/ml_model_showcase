# ML Model Deployment Showcase

A full-stack ML model deployment showcase using **FastAPI** for the backend and **Flutter** for the frontend. This project simulates a production-level interface for testing and visualizing deployed machine learning models, with support for logging and performance insights.

---

##  Tech Stack

**Frontend**
- Flutter (Dart)
- Material Design Components
- HTTP integration with backend
- Input forms, result dashboards, and prediction logs

**Backend**
- FastAPI (Python)
- Pydantic for schema validation
- SQLite for simple logging
- Simulated model response (can be extended to real ML model)
- REST APIs for predictions and logs

---

##  Features

- Upload input for ML prediction via a Flutter UI
- View prediction results in real-time
- View log history of past predictions
- Full API backend with schema validation
- Ready-to-extend with actual ML model (plug-in support)
- Easily portable and modifiable

---

##  Project Structure

ml_model_showcase/
├── backend/
│ ├── config/
│ │ └── .env.example
│ ├── database/
│ │ └── db.py
│ ├── logs/
│ │ └── logger.py
│ ├── models/
│ │ └── dummy_model.py
│ ├── routes/
│ │ └── predict.py
│ ├── schemas/
│ │ └── input_output.py
│ ├── services/
│ │ └── predict_service.py
│ ├── main.py
│ └── requirements.txt
├── frontend/
│ ├── lib/
│ │ ├── main.dart
│ │ ├── screens/
│ │ └── widgets/
│ ├── android/ ios/ web/ etc.
│ └── pubspec.yaml
└── README.md

yaml
Copy
Edit

---

##  Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
API available at http://localhost:8000

Frontend (Flutter)
bash
Copy
Edit
cd frontend
flutter pub get
flutter run
Make sure a device/emulator is running.

 API Endpoints
Method	Endpoint	Description
POST	/predict	Submit input, get prediction
GET	/logs	View all past logs

Environment Variables
env
Copy
Edit
# backend/config/.env.example

DATABASE_URL=sqlite:///./ml_logs.db

 Future Enhancements
Plug in a real ML model (TensorFlow, PyTorch, etc.)

Add user authentication (JWT or Firebase)

Deploy backend on AWS / GCP

Dockerize for production

Improve UI with charts and filters

License
This project is open-source and free to use.