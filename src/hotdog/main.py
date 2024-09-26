from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
from fastapi import FastAPI, File, UploadFile
from datetime import datetime
from pytz import timezone
import pymysql.cursors
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
    file_name = file.filename
    file_ext = file.content_type.split("/")[-1] #"image/png"
    upload_dir = os.getenv("UPLOAD_DIR",'/home/hahahellooo/code/hnh/img')
    predict = predit()
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir, exist_ok=True)
    import uuid
    file_full_path = os.path.join(upload_dir, f'{uuid.uuid4()}.{file_ext}')
    
    with open(file_full_path, "wb") as f:
        f.write(img)

    return  {
               "file_name" : file.filename,
               "content_type" :file.content_type,
               "file_full_path":file_full_path,
               "prediction":predict
            }

def predict():
    result = {"Hello":random.choice(["This is a hotdog","This is not a hotdog"])}


    return result
