from fastapi import HTTPException, status, Security, FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery
import json
import uvicorn
import requests
import testAPI

api_keys = [
    "4ae9400a1eda4f14b3e7227f24b74b44"
]




app = FastAPI()


@app.get("/public")
#def public():
   # """a public endpoint that does not require any authentication."""
   # return "Public Endpoint"

@app.get("/store")
def get_store_details():
    url = "https://apimdev.wakefern.com/mockexample/V1/getStoreDetails"
    header = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44', "User-Agent": "PostmanRuntime/7.36.3",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    print(response)
    return response.text

@app.get("/item")
def get_store_details():
    url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"
    header = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44', "User-Agent": "PostmanRuntime/7.36.3",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    data = json.loads(response.content)
    # Check if 'hits' key exists and it has at least one item
    if 'hits' in data and len(data['hits']) > 0:
        # Extract ingredients from the first recipe
        Description = data['hits'][0]['item']['d']
        return Description
    else:
        return {"message": "No item found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
    
