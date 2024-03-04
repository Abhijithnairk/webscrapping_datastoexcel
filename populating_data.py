from flask import Flask
import json
import requests
import pandas as pd

app = Flask(__name__)

def item_parser(category, search_term, site):
    with open('competitors.json', 'r') as file:
        competitor = json.load(file)[site]     
    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': competitor['cookie']
    }
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if data.get('items'):
        items = data.get('items')
        for item in items:
            categories = item['categories']
            for category_dict in categories:            
                if category in category_dict['name'].lower():
                    if search_term in item['name'].lower():
                        item_found = {
                            "site":site,
                            "name": item['name'],
                            "price": item['base_price'],
                        }
                        return {"item": item_found}
    return {"message": "Item not found"}

# @app.route('/api/v1/getitem/<site>/<category>/<searchterm>')   

df = pd.read_excel('aimart.xlsx')


for index,row in df.iterrows():
    # print(row['name'])
    #print(row)
    search_term=row['name']
    category=row['category']
    for site in ['tfm','sprouts','wegmans']:
        result=item_parser(category, search_term, site)
        print(result)
        
        if "status" in result and result["status"]==200:
            df.at[index,f'{site} name']=result['item']['name']
            df.at[index,f'{site} price']=result['item']['price']
        else:
            df.at[index,f"{site}_name"] = "Not found"
            df.at[index,f"{site}_price"] = "N/A"
            
df.to_excel("updated_excel_file.xlsx",index=False)

if __name__ == '__main__':
    # Debug mode
    app.run(debug=True, port=8000)
