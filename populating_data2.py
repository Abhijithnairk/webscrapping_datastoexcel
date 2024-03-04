import pandas as pd
import json
import requests

def item_parser(category, search_term, site):
    with open('competitors.json', 'r') as file:
        competitor = json.load(file)[site]     
    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
    }
    status = 404
    item_found = "No item Found"
    response = requests.get(URL, headers=HEADERS)   
    data = response.json()
    if(data.get('items')):
        items = data.get('items')
        for item in items:
            categories = item['categories']
            for category_dict in categories:            
                if category in category_dict['name'].lower() and search_term in item['name'].lower():
                    item_found = {
                        "name": item['name'],
                        "price": item['base_price'],
                    }
                    status = 200
                    break   
        return {"status": status, "item": item_found}
    else:
        return {"data": data}

# Read the Excel file
df = pd.read_excel('aimart.xlsx')


for index, row in df.iterrows():

    search_term = row['name']
    category = row['category']
    
   
    for site in ['sprouts', 'wegmans', 'tfm']:
         
        result = item_parser(category, search_term, site)
       
        print(result)
        
        
        if "status" in result and result["status"] == 200:
            # df.at[index, f'{site}_name'] = result["item"]["name"]
            df.at[index, f'{site}_price'] = result["item"]["price"]
        else:
            df.at[index, f'{site}_name'] = "Not Found"
            df.at[index, f'{site}_price'] = "N/A"


df.to_excel('updated_excel_file2.xlsx', index=False)