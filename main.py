import logging

from docarray import Document, DocumentArray
from docarray.document.pydantic_model import PydanticDocument
from fastapi import FastAPI

app = FastAPI()

local_backup_fn = 'data.bin'
import os
images = DocumentArray.empty()
if os.path.exists(local_backup_fn):
    try:
        images = DocumentArray.load_binary(local_backup_fn)
        logging.info(f'loading data from {local_backup_fn} completed, size {len(images)}')
    except Exception as e:
        logging.warning(f'loading data from {local_backup_fn} failed')

@app.get('/images')
async def get_images(skip: int = 0, limit: int = 3):
    return {
        'images': [
            {
                'caption': f'{d.tags["description"]}',
                'author': f'{d.tags["author"]}',
                'timestamp': f'{d.tags["ctime"]}',
                'uri': f'{d.uri}'
            } for d in images[skip:skip + limit]
        ]
    }


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
