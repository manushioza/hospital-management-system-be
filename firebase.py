import firebase_admin
from firebase_admin import db, firestore, credentials

# Fetch the service account key JSON file contents
cred = credentials.Certificate('coe892hms-firebase-adminsdk-qmde8-c8ff65daf4.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'doctor')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')