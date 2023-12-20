from fastapi import FastAPI
from buymeacoffee import Purchase
from db import get_purchases, insert_purchase

app = FastAPI()

@app.get("/")
def index():
    return {"Please Subscribe":"youtube.com/@programmerqdev"}

@app.get("/latest")
def latest_message():


@app.post("/bmc")
def bmc(purchase: Purchase):
    print(purchase)
    result: bool = insert_purchase(purchase)
    return {"status": result, "latest_purchase" : get_purchases(latest=True), "purchases": get_purchases()}

if __name__ == '__main__':
    app.run()
