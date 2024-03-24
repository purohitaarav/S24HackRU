
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
import json
import Recipes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


API_KEY = "4ae9400a1eda4f14b3e7227f24b74b44"

def get_api_response(url):
    header = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        "User-Agent": "PostmanRuntime/7.36.3",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="API request failed")
    return response.json()

@app.get("/store")
def get_store_details():
    url = "https://apimdev.wakefern.com/mockexample/V1/getStoreDetails"

    header = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44', "User-Agent": "PostmanRuntime/7.36.3",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    print(response)
    return json.loads(response.text)
    
@app.get("/item")
def get_item_details(recipe: str = "chicken"):
    
    url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"
    header = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44', "User-Agent": "PostmanRuntime/7.36.3",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=header)
    data = json.loads(response.content)
    print(data)
    # Check if 'items' key exists and it has at least one item
    if len(data) > 0:
        # Extract name and price of all items
        response = {}
        recipes = Recipes.get_recipe_details(recipe)
        for ingredients in recipes:
            found = False
            for item in data:
                if item['Description'].lower() in ingredients["food"].lower():
                    response[ingredients["food"]] = {"Price": item['Price']}
                    found = True
                    break
                if not found:
                     response[ingredients["food"]] = {ingredients["food"] + " cannot be found in a Wayfern store near you"}
        #for item in data:
           # response[item['Description']] = {
            #    "Price": item['Price'],
             #   "Digital Coupon": item["Digital Coupon"]
           # }
        return response
   # else:
     #   return {"message": "No items found"}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)


