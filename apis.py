import requests
import os
from dotenv import load_dotenv

load_dotenv()



#### --------- Get Product from internal api --------- ####
HOST = os.getenv('HOST')
SHOP_IDENTIFIER = os.getenv('SHOP_IDENTIFIER')
TOKEN = os.getenv('TOKEN')
APP_SLUG = os.getenv('APP_SLUG')

url = HOST + "/products/v2/shops/" + SHOP_IDENTIFIER + "/apps/" + APP_SLUG + "/products?deep=true&page=1&limit=20"
headers = {'Authorization': TOKEN}


r = requests.get(url,headers=headers)
respone_json = r.json()
print(respone_json)
