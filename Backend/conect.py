import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

credential = credentials.Certificate("Chave-de-Conta/bylimas-osgabis-firebase-adminsdk-fbsvc-e1e38745eb.json")
app = firebase_admin.initialize_app(credential)

db = firestore.client()

print("Banco conectado!")
