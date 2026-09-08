from fastapi import FastAPI

app = FastAPI()


# run: fastapi dev main.py

@app.get("/")
def home():
    return "Welcome to Fastapi Series !"

@app.get("/connect")
def contact():
    return "Connect any time"