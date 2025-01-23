# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI, Query, Request
import os
from typing import List
from functions import get_all_data, get_data_for_class
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins

#@app.get("/")
#async def root():
#    return {"message": "Hello!"}
#

@app.get("/api")
async def return_data(class_parameter: List[str] = Query([], alias="class")):
    if class_parameter:
        #print(classes)
        #split_params = q.split(r'&')
        #class_names = [x.split('=')[1] for x in split_params]
        print(f"{class_parameter}")
        output = get_data_for_class(class_parameter)
    else:
        print("Returning all data as no query parameter received")
        output = get_all_data()
    return output


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)