from fastapi import FastAPI, Request 
from mockData import products

app = FastAPI()


# run: fastapi dev main.py

@app.get("/")
def home():
    return "Welcome to Fastapi Series !"


@app.get("/products")
def get_products():
    return products

# path Parameters
@app.get("/product/{product_id}")
def get_products(product_id:int):
    for i in products:
        if product_id == i.get("id"):
            return i
    
    return {
        "error":"Product not found"
    }

# query parameter
@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet": f"Hello {name}, Your age is {age}"
    }


# query parameter via request
@app.get("/greet2")
def greet_user(request:Request):
    
    query_params= dict(request.query_params)

    return {
        "greet": f"Hello {query_params.get("name")}, Your age is {query_params.get("age")}"
    }