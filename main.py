# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI
import os
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

@app.get("/api")
async def return_all_data():
    data_path = os.path.join('q-fastapi.csv')
    
    return {"message": "Hello!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)