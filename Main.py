from fastapi import HTTPException, status, Security, FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery
import json
import uvicorn
import requests


api_keys = [
    "my_api_key"
]

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_api_key(
        api_key_header: str = Security(api_key_header),
) -> str:
    if api_key_header in api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


app = FastAPI()


@app.get("/public")
def public():
    """a public endpoint that does not require any authentication."""
    return "Public Endpoint"


@app.get("/protected")
def private(api_key: str = Security(get_api_key)):
    """a private endpoint that requires a valid API key to be provided."""
    return f"Private Endpoint. API Key: {api_key}"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
def main():
    url = "https://apimdev.wakefern.com/mockexample/V1/getItemDetails"  # Replace this with your API endpoint
    api_key = "4ae9400a1eda4f14b3e7227f24b74b44"  # Replace this with your subscription key
   
    params = {'Ocp-Apim-Subscription-Key': '4ae9400a1eda4f14b3e7227f24b74b44'}

    response = requests.get(url, params=params)
    print(response.text)