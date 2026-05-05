from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()



@app.get('/')
async def root():
    return{"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return{"message":"This is my API page !"}
#How do we rettive the data that we sent in the body
@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):#assign the body to payload variable and assign a tyoe dict = body(..)
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}#This will extract all of the fields from the body