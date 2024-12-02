import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('adpm-1be79-firebase-adminsdk-6fasg-fa1b1ea8ea.json')
firebase_admin.initialize_app(cred)

# Get a Firestore database reference
db = firestore.client()
