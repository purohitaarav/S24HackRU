from fastapi import HTTPException, status, Security, FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery
import json
import uvicorn
import requests
import testAPI

api_keys = [
    "4ae9400a1eda4f14b3e7227f24b74b44"
]


#iokay

app = FastAPI()


@app.get("/public")
#def public():
   # """a public endpoint that does not require any authentication."""
   # return "Public Endpoint"


@app.get("/recipe")
def get_recipe_details(search_for):
    food = search_for
    url = 'https://api.edamam.com/api/recipes/v2?type=public&beta=false&q={food}&app_id=ac2cee73&app_key=813286124be5b0c3817b0fb7f8034476'.format(food = food)
    response = requests.get(url)
    data = json.loads(response.content)
    # Check if 'hits' key exists and it has at least one item
    if 'hits' in data and len(data['hits']) > 0:
        # Extract ingredients from the first recipe
        ingredients = data['hits'][0]['recipe']['ingredients']
        return ingredients
    else:
        return {"message": "No recipe found for {}".format(food)}

    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
    