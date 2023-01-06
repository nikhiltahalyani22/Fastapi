from typing import Optional
from unittest import async_case
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async  def index():
    return {'data': {'name': {'Nikks'}}}

@app.get('/blog/unpublised')
async  def unpublised():
    return {'data': "I don't Know" } 

@app.get('/blog/{id}')
async  def show(id:int):
    return {'data': id }

@app.get('/blog/{id}/comments')
async  def comments(id, limit:int =10):
    return {'data': {id :["What", limit ]} }

@app.get('/blog')
async def blog(limit =1222 , published :bool = True, sort: Optional[str] =None):
    if published:
        return{'hey'}
    else:
        return {'data': {f" limit is {limit}"}}

class Blog(BaseModel):
    tittle: str
    body: str
    published: Optional[bool]    

@app.post('/blog')
def create_blog(request: Blog):
    return { 'data' : f"Blog is created with tiile as {request}"}


#if __name__== "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)