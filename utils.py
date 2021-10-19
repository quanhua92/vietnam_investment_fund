import requests
import json
from datetime import datetime

def get_all_products():
    url = "https://api.fmarket.vn/res/products/filter"
    data = {"types":["NEW_FUND","TRADING_FUND"],"issuerIds":[],"page":1,"pageSize":1000,"fundAssetTypes":[],"bondRemainPeriods":[],"searchField":""}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    x = requests.post(url, json=data, headers=headers)
    return json.loads(x.text)

def get_history(product_id):
    url = "https://api.fmarket.vn/res/product/get-nav-history"
    toDate = datetime.now().strftime("%Y%m%d")
    data = {"isAllData":1,"productId":product_id,"fromDate": None, "toDate": toDate}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    x = requests.post(url, json=data, headers=headers)
    return json.loads(x.text)