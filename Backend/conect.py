import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

credential = credentials.Certificate("")
app = firebase_admin.initialize_app(credential)

db = firestore.client()


