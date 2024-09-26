from typing import Annotated
import os
from fastapi import FastAPI, File, UploadFile
from datetime import datetime
from pytz import timezone
import pymysql.cursors

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    img = await file.read()
    file_name = file.filename
    file_ext = file.content_type.split("/")[-1] #"image/png"
    upload_dir = os.getenv("UPLOAD_DIR",'/home/hahahellooo/code/hnh/img')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir, exist_ok=True)
    import uuid
    file_full_path = os.path.join(upload_dir, f'{uuid.uuid4()}.{file_ext}')
    
    with open(file_full_path, "wb") as f:
        f.write(img)

    return  {
               "file_name" : file.filename,
               "content_type" :file.content_type,
               "file_full_path":file_full_path
            }

