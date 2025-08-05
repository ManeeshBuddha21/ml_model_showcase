from fastapi.responses import JSONResponse
import sqlite3
import os

@router.get("/logs")
def get_prediction_logs():
    db_path = os.path.join("logs", "predictions.db")
    if not os.path.exists(db_path):
        return JSONResponse(status_code=404, content={"message": "Log database not found"})

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, model_name, input_text, predicted_label, confidence, timestamp FROM predictions ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "model_name": row[1],
            "input_text": row[2],
            "predicted_label": row[3],
            "confidence": row[4],
            "timestamp": row[5],
        })

    return {"logs": logs}
