import firebase_admin
from firebase_admin import credentials, firestore
import threading
import time
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
import requests
import os
from scanner import process_upc
from dataLayer import get_db
import re

load_dotenv()

count = 0
quota = 200

print('Initializing Firestore connection...')
db = get_db()
print('Initialized')

# Create an Event for notifying main thread.
callback_done = threading.Event()

def get_body(image_data):
    image64 = image_data.replace('data:image/png;base64,', '').replace('data:image/jpeg;base64,', '')
    body = {
        "requests": [
            {
                "image" : {
                    "content": image64
                },
                "features":[
                    {
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    }
    return body

def process_image(image_data):
    global count
    global quota
    print('Processing image...')

    if count < quota:
        count += 1
        print(count)
        body = get_body(image_data)
        response = requests.post('https://vision.googleapis.com/v1/images:annotate?key=' + os.getenv('GOOGLE_API_KEY'), json=body)
        print(response.json()["responses"][0]["fullTextAnnotation"]["text"])
        text = response.json()["responses"][0]["fullTextAnnotation"]["text"]
        print('Image processed')
        return text

    else:
        print('Quota exceeded, blocked')
        exit()

def extract_upcs(text):
    print("Extracting UPCs...")
    upcs = []
    matches = re.findall("\n\d{9}\n", text, re.M)
    for match in matches:
        upcs.append(match.replace("\n", ""))
    print("Extracted")
    return upcs

def handle_image(image_data):
    rawText = process_image(image_data)
    upcs = extract_upcs(rawText)
    print(upcs)
    for upc in upcs:
        process_upc(upc)


# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.id}')
        data = doc.to_dict()
        handle_image(data['data'])
    callback_done.set()

doc_ref = db.collection(u'images').document(u'receipt')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)


def main():
    while True:
        print('listening...')
        time.sleep(300)


if __name__ == "__main__":
    main()
