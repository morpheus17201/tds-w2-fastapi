# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI
import os
from functions import get_all_data, get_data_for_class


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello!"}

@app.get("/api")
async def return_all_data():
    output = get_all_data()
    return output

@app.get("/api/{class_names}")
async def return_class_data(class_names):
    
    return output



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)