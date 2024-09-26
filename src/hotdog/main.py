from transformers import pipeline
from fastapi.templating import Jinja2Templates
import os
from fastapi import FastAPI, File, UploadFile
from datetime import datetime
import random
from fastapi import Request

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "🌭hotdog🌭"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSczt3ABqLESuSYrykIdfJvg26VGsg21Qp0Pg&s"
    dog = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhVhtuh5vDwhVV5WB68N5tAo6IqwoVusaNaQ&s"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url":image_url})
    

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img)) # 이미지 바이트를 PIL 이미지로 변환
    p = model(img)
    from hotdog.util import get_max_score
    message = get_max_score(p)
    return message
    
#def predict():
#    result = {"Hello":random.choice(["This is a hotdog","This is not a hotdog"])}


#    return result
