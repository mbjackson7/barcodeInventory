import firebase_admin
from firebase_admin import credentials, firestore
db = firestore.client()  # this connects to our Firestore database
collection = db.collection('places')  # opens 'places' collection

def in_database(UPC):
    pass

def increment_quantity(UPC):
    pass

def add_item(data):
    pass