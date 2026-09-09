from fastapi import FastAPI, Request 
from mockData import products
from dtos import ProductDTO


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


## Different Types of HTTP METHODS

# 2. post
# Types of Post Ways: body, headers, query_params

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    
    print(product_data)
    product_data = product_data.model_dump()
    print(product_data)
    products.append(product_data)

    return {"status":"Product Created Successfully...","New Data":products}



# 3. put
@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):

    for index,x in enumerate(products):
        if x.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status":"Product Updated Successfully...","New Data":products}
            
    return {
        "error": "Product Not Found for this ID"
    }


# 1. delete
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):

    for index, x in enumerate(products):
        if x.get("id") == product_id:
            delete_product = products.pop(index)
            return {
                "status":"Product Removed Successfully...",
                "New Data":products
            }

    return {
        "error": "Product Not Found for this ID"
    }
            