from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TELEGRAM_TOKEN = "8024389457:AAFOuNZr9Nb29lCa99TCWfvGv3pub8BwqaM"
CHAT_ID = 5599230987


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.post("/send")
async def send_message(request: Request):
    data = await request.json()
    message = data.get("message")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=payload)
    return {"status": response.status_code, "response": response.json()}
