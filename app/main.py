from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from google.cloud import firestore
from datetime import datetime
from app.firebase_config import db  # Import Firestore client

app = FastAPI()

@app.post("/Image")
async def save_data(request: Request):
    try:
        data = await request.json()  # Get JSON data from the request

        # Ensure required fields are present
        required_fields = ["Category", "DFU_Image", "Date", "Patient_ID"]
        if not all(field in data for field in required_fields):
            return JSONResponse({"error": "Missing required fields"}, status_code=400)

        # Convert Date to Firestore Timestamp
        try:
            data["Date"] = firestore.Timestamp.from_datetime(
                datetime.fromisoformat(data["Date"])
            )
        except ValueError:
            return JSONResponse({"error": "Invalid Date format"}, status_code=400)

        # Save data to Firestore
        doc_ref = db.collection("Image").document()  # Auto-generate document ID
        doc_ref.set(data)

        return JSONResponse({"message": "Data saved successfully"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
