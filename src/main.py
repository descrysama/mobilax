from login import login;
from data_handler import add_data, remove_at_start;
import json;
import os
import requests
from dotenv import load_dotenv
from config_db import getMobilaxLinks
load_dotenv()


result = getMobilaxLinks()

remove_at_start(os.getenv("OUTPUT_PATH"))
for i, link in enumerate(result[0:], start=0):
    items_list = []
    print(json.dumps({'MOBILAX': (str(i+1) + " / " + str(len(result)))}))
    data_response = requests.get(result[0][0], cookies={"token": login()})
    if data_response.status_code == 200:
        json_data = data_response.json()
        for product in json_data['products'] :
            item = ["", ""]
            item[0] = str(product['ean13'])
            item[1] = str(product['price']['price']).replace('.', ',')
            items_list.append(item)
        add_data(os.getenv("OUTPUT_PATH"), items_list)
    else:
        print("url not found mind replacing it here is the index's list: ", i)