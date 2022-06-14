import os
import requests
from dotenv import load_dotenv





def get_info(UPC):
    API_KEY = os.getenv('API_KEY')
    requestString = "https://api.upcdatabase.org/product/" + str(UPC) + "?apikey=" + str(API_KEY)
    response = requests.get(requestString)
    if response.status_code == 200:
        print('Success!')
        return response.json()
    else:
        return None
        

def main():
    load_dotenv()
    #Test UPC, from Matzos
    UPC = "0070227500010"
    data = get_info(UPC)
    if data:
        print

if __name__ == "__main__":
    main()
