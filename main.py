import logging
import os

from docarray import Document, DocumentArray
from docarray.document.pydantic_model import PydanticDocument
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

local_backup_fn = 'data.bin'

images = DocumentArray.empty()
if os.path.exists(local_backup_fn):
    try:
        images = DocumentArray.load_binary(local_backup_fn)
        logging.info(f'loading data from {local_backup_fn} completed, size {len(images)}')
    except Exception as e:
        logging.warning(f'loading data from {local_backup_fn} failed')



class IdOnly(BaseModel):
    id: str


@app.get('/images')
async def get_images(skip: int = 0, limit: int = 3):
    return images[skip:skip + limit].to_pydantic_model()


@app.get('/image_ids', response_model=IdOnly)
async def get_image_ids():
    return images


@app.post('/images')
async def post_images(item: PydanticDocument):
    doc = Document.from_pydantic_model(item)
    images.append(doc)
    try:
        images.save_binary(local_backup_fn)
        logging.info(f'saving data completed, total images: {len(images)}')
    except Exception as e:
        logging.error(f'saving data failed, {e}')
    return {
        'message': 'image added',
        'total': len(images)
    }
