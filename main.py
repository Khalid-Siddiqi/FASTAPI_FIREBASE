from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from FASTAPI-FIREBASE.firebase_config import db  # Import the Firestore client

app = FastAPI()

@app.post("/Image")
async def save_data(request: Request):
    data = await request.json()  # Get data from Postman

    # Ensure required fields are present
    if not all(field in data for field in ["Category", "DFU_Image", "Date", "Patient_ID"]):
        return JSONResponse({"error": "Missing required fields"}, status_code=400)

    # Convert Date to a Firestore Timestamp
    try:
        data["Date"] = firestore.Timestamp.from_datetime(data["Date"])
    except ValueError:
        return JSONResponse({"error": "Invalid Date format"}, status_code=400)

    # Save data to Firestore
    doc_ref = db.collection('Image').document()  # Replace 'your_collection'
    doc_ref.set(data)

    return JSONResponse({"message": "Data saved successfully"})
