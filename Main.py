import requests
<<<<<<< HEAD
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
=======
import json
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

def fetch_json_data(url, subscription_key):
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def main():
    api_url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"  # Replace this with your API endpoint
    subscription_key = "4ae9400a1eda4f14b3e7227f24b74b44"  # Replace this with your subscription key
    json_data = fetch_json_data(api_url, subscription_key)
    if json_data:
        # Process the JSON data as needed
        print(json.dumps(json_data, indent=4))  # Example: printing the JSON data
>>>>>>> 5d611edadbaf835c7ffbf9a971cfff5d0850dd50

        # You can further process the JSON data here...

if __name__ == "__main__":
<<<<<<< HEAD
    uvicorn.run(app, host="0.0.0.0", port=8001)
    
=======
    main()
>>>>>>> 5d611edadbaf835c7ffbf9a971cfff5d0850dd50
