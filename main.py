from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import pandas as pd
from ai_service import generate_summary
from email_service import send_email

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), email: str = Form(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Upload CSV only")

    df = pd.read_csv(file.file)

    summary = generate_summary(df)

    try:
        send_email(email, summary)
    except Exception as e:
        print("Email failed:", e)

    return {"status": "success", "summary": summary}