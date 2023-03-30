from fastapi import FastAPI 

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
) 


@app.get("/hello")
async def hello_world():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def hello_workshop(item_id):
    return {"item_id": item_id}
