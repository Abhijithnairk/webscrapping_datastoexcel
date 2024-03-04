from flask import Flask
import json
import requests
app = Flask(__name__)
import pandas as pd

def item_parser(category, search_term,site):
    with open('competitors.json', 'r') as file:
        competitor = json.load(file)[site]     
    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
    }
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if(data.get('items')):
        items=data.get('items')
        # # items_df = pd.DataFrame(data.get('items'))
        for item in items:
            categories=item['categories']
            for category_dict in categories:            
                if category in category_dict['name'].lower():
                    if search_term in item['name'].lower():
                        item_found={
                                    "name":item['name'],
                                    "price":item['base_price'],
                                    }
                        
        #                 break   
    #     return ({ "item": item_found})
    # else:
    #     return ({"data": data})
        
#sample url: http://127.0.0.1:5000/api/v1/getitem/wegmans/apples/apple
df=pd.read_excel('aimart.xlsx')

for index,row in df.iterrows():
    # print(row['name'])
    # print(row['category'])
    search_term=row['name']
    category=row['category,']
    for site in['sprouts','wegmans','tfm']:

@app.route('/api/v1/getitem/<site>/<category>/<search_term>')   

def getitem(category,search_term,site):
        return(item_parser(category,search_term,site))

if __name__ == '_main_':
#    debug mode
    app.run(debug=True, port=8000)


# import pandas as pd

# data={'name':['sanjay','yasin','arya'],
#         'age':[25,40,85],
#         'city':["pattambi","balussery","ulliyeri"]}

# df=pd.DataFrame(data)

# print(df)

# for index,row in df.iterrows():
#     print("index",index)
#     print(row)
#     print()