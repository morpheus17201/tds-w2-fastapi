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
import csv

app = FastAPI()

students = []
with open('q-fastapi.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })


app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins

#@app.get("/")
#async def root():
#    return {"message": "Hello!"}
#

@app.get("/api")
async def return_data(class_parameter: List[str] = Query([], alias="class")):
    if class_parameter:
        print(f"{class_parameter}")
        selected = [student for student in students if student['class'] in class_parameter]
        return {"students":selected}
    else:
        print("Returning all data as no query parameter received")
        #output = get_all_data()
        return {"students":students}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)