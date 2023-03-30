from fastapi import FastAPI 

app = FastAPI() 

@app.get("/hello")
async def hello_world():
    return {"Hello": "Worlds"}

@app.get("/items/{item_id}")
async def hello_workshop(item_id):
    return {"item_id": item_id}
