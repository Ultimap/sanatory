import os
from fastapi import UploadFile
from app.config import img_folder


async def add_img(img: UploadFile):
    os.makedirs(img_folder, exist_ok=True)
    img_path = os.path.join(img_folder, img.filename)
    with open(img_path, 'wb') as file:
        content = await img.read()
        file.write(content)