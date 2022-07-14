#!/usr/bin/env python3

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory=".")
 
@app.get("/")
async def test(request : Request):
    return templates.TemplateResponse("home.html", {"request":request}) 



@app.get("/api/bmi")
def coba(request:Request, height: float, weight: float):
    
    BMI = round(weight/(height * height))

    # height = float(input("enter your height in m: "))
    # weight = float(input("enter your weight in kg: "))
    
    if BMI < 18.5:
        label = "underweight"
    elif  BMI < 25 :
        label = "normal"
    elif BMI >= 25 :
        label = "overweight"
    
    return templates.TemplateResponse("result.html",{
        "request": request,
        "height" : height,
        "weight" : weight,
        "BMI" : BMI,
        "label": label
    })