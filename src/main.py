from login import login;
from data_handler import add_data, remove_at_start;
import json;
import requests


with open('var/www/scripts/mobilax/src/urls.json', 'r') as file:
    json_data = json.load(file)

urls = json_data['urls']

remove_at_start('var/www/scripts/mobilax/src/output.xlsx')

for i, url in enumerate(urls) :
    items_list = []
    print(json.dumps({'MOBILAX': (str(i+1) + " / " + str(len(urls)))}))
    data_response = requests.get(url, cookies={"token": login()})
    if data_response.status_code == 200:
        json_data = data_response.json()
        for product in json_data['products'] :
            item = ["", ""]
            item[0] = str(product['ean13'])
            item[1] = str(product['price']['price']).replace('.', ',')
            items_list.append(item)
        add_data('var/www/scripts/mobilax/src/output.xlsx', items_list)
    else:
        print("url not found mind replacing it here is the index's list: ", i)