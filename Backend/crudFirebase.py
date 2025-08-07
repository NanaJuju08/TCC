import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

credential = credentials.Certificate("Chave-de-Conta/bylimas-osgabis-firebase-adminsdk-fbsvc-e1e38745eb.json")
app = firebase_admin.initialize_app(credential)
 
db = firestore.client()

print("Banco conectado!")


#### LER DADOS DO FIRESTORE
def read():
    productsRef = db.collection("products")
    productsDocs = productsRef.stream()

    for doc in productsDocs:
        product = doc.to_dict()
        print(f"PRODUTO: \nName: {product['name']} \nId: {doc.id}")

#### ADICIONAR DADOS NO FIRESTORE
def create():
    product = {
        'name': 'copo'
    }

    productRef = db.collection("products").add(product)
    print("Produto adicionado!")


### EXCLUIR DADOS NO FIRESTORE
print("Escolha o produto a ser deletado: ")
read()
productId = input("Id: ")

try:
    db.collection("product").document(f"{productId}").delete()
    print("Produto deletado!")
except Exception as e:
    print(f"Problema ao deletar: {e}")

