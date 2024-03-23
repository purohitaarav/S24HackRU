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

@app.get("/recipe")
def get_recipe_details():
    url = "https://api.edamam.com/api/recipes/v2"
    header = {'app_key': '813286124be5b0c3817b0fb7f8034476',
               "Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    print(response.content)
    return response.content


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
    
