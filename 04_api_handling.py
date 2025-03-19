#import request and random for random data 
# add virtual environment for pc safety ig

import requests 
import random 

def jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    deta = requests.get(url)
    data_in_json = deta.json()
    if data_in_json["success"] and "data" in data_in_json :
        data_from_api = data_in_json["data"]
        joke = data_from_api["data"]
        listt = [x for x in joke]
        number  = random.choice(listt)
        content = number["content"]
        jock = print(str(content))
        return jock  
    
    else :
        Exception("FAILtoFETCH")


def main():
    try :
        jokes()
    except Exception as e :
        print(str(e))       


if __name__ == "__main__" :
    main()
