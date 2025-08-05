import sqlite3
import os

DB_PATH = os.path.join("logs", "predictions.db")

def log_prediction(model_name: str, input_text: str, predicted_label: str, confidence: float, timestamp):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            input_text TEXT,
            predicted_label TEXT,
            confidence REAL,
            timestamp TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO predictions (model_name, input_text, predicted_label, confidence, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (model_name, input_text, predicted_label, confidence, timestamp.isoformat()))

    conn.commit()
    conn.close()
