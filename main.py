from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from .firebase_config import db  # Import the Firestore client

app = FastAPI()

@app.post("/image")
async def save_data(request: Request):
    data = await request.json()  # Get data from Postman

    # Save data to Firebase (example using Cloud Firestore)
    doc_ref = db.collection('image').document()
    doc_ref.set(data)

    return JSONResponse({"message": "Data saved successfully"})
