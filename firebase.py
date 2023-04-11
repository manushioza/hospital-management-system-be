import firebase_admin
from firebase_admin import db, firestore, credentials

# Fetch the service account key JSON file contents
cred = credentials.Certificate('coe892hms-firebase-adminsdk-qmde8-c8ff65daf4.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

