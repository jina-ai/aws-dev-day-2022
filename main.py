from fastapi import FastAPI
from docarray import Document
from docarray.document.pydantic_model import PydanticDocument

from utils import load_data, logger

app = FastAPI()

da_name = 'aws_china_dev_day_demo_202208_cn'
images = load_data(da_name)


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
        images.push(name=f'{da_name}_alpha')
        logger.info(f'pushing data completed, total images: {len(images)}')
    except Exception as e:
        logger.error(f'pushing data failed, {e}')
    return {
        'message': 'image added',
        'total': len(images)
    }
