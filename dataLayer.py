import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
collection = db.collection('pantry')

def in_database(UPC):
    docRef = collection.document(str(UPC))
    if docRef.get().exists:
        return True
    else:
        return False


def increment_quantity(UPC, quantity:int=1):
    docRef = collection.document(str(UPC))
    docRef.update({'quantity': firestore.Increment(quantity)})

def add_item(data):
    collection.document(str(data["upc"])).set(data)