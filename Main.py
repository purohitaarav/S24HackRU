import requests
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

        # You can further process the JSON data here...

if __name__ == "__main__":
    main()