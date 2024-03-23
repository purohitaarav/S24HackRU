from fastapi import FastAPI, HTTPException, Header
import requests

app = FastAPI()

@app.get("/getStoreDetails")
def get_store_details(api_key: str = Header(None)):
    if api_key != "4ae9400a1eda4f14b3e7227f24b74b44":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    url = "https://apimdev.wakefern.com/mockexample/V1/getStoreDetails"
    headers = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44'}
    response = requests.get(url, headers=headers)
    return response.text

@app.get("/getItemDetails")
def get_item_details(api_key: str = Header(None)):
    if api_key != "4ae9400a1eda4f14b3e7227f24b74b44":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"
    headers = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44'}
    response = requests.get(url, headers=headers)
    return response
