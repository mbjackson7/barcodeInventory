import os
import requests
from dotenv import load_dotenv
from dataLayer import in_database, increment_quantity, add_item

def get_data(UPC):
    API_KEY = os.getenv('API_KEY')
    requestString = "https://api.upcdatabase.org/product/" + str(UPC) + "?apikey=" + str(API_KEY)
    response = requests.get(requestString)
    if response.status_code == 200:
        print('Success!')
        return response.json()
    else:
        return None
        
def initialize_data(UPC):
    rawData = get_data(UPC)
    data = {}
    if rawData["title"] != "":
        data["title"] = rawData["title"]
    else:
        data["title"] = rawData["description"]
    data["UPC"] = UPC
    data["quantity"] = 1
    data["price"] = None
    data["notes"] = None
    data["lowNum"] = 0
    return data


def main():
    load_dotenv()
    #Test UPC, from Matzos
    UPC = "0070227500010"

    if in_database(UPC):
        increment_quantity(UPC)
    else:        
        data = initialize_data(UPC)
        add_item(data)


if __name__ == "__main__":
    main()
