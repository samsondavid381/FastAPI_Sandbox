from fastapi import FastAPI
from pydantic import BaseModel


#Pydantic Model
class MessagePayload(BaseModel):
    message : str

#FastAPI
app = FastAPI()
@app.get("/")
async def helloMessage():
    return {"message":"hello"}
@app.post("/classify-mo", response_model=MessagePayload , description="Returns the JSON Payload sent in the request")
async def classifyMO(payload: MessagePayload):
    return payload