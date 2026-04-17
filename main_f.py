from fastapi import FastAPI
from search import search_products
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Ajio search API"}

@app.get("/search/{query}")
def search(query: str):
    if len(query)<2:
        return {"Error": "Query must be at least 2 characters long."}
    return search_products(query)