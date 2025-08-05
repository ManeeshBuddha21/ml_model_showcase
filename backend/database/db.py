import sqlite3
import os

def init_db():
    db_path = os.path.join("logs", "predictions.db")
    os.makedirs("logs", exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Just ensures table is created (redundant safety)
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

    conn.commit()
    conn.close()
