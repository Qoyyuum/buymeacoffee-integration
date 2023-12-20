from fastapi import FastAPI
from buymeacoffee import Extras, Purchase, PurchaseData

app = FastAPI()

@app.get("/")
def index():
    return {"Please Subscribe":"youtube.com/@programmerqdev"}

@app.post("/bmc")
def bmc(purchase: Purchase):
    print(purchase)
    return {"status": "OK"}

if __name__ == '__main__':
    app.run()
