from fastapi import FastAPI
import os
from docarray import Document, DocumentArray
from docarray.document.pydantic_model import PydanticDocument


app = FastAPI()


def load_data(name):
    if os.environ.get('JINA_AUTH_TOKEN', None) is not None:
        try:
            da = DocumentArray.pull(name=name)
            return da
        except Exception as e:
            print(f'加载数据失败, {e}')
    else:
        print('JINA_AUTH_TOKEN is not set')


da_name = 'aws_china_dev_day_demo_202208_cn'
images = load_data(da_name)
# images = DocumentArray.load_binary('data.bin')


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
    images.push(name=f'{da_name}_alpha')
    return {
        'message': 'image added',
    }

from starlette.testclient import TestClient
client = TestClient(app)

response = client.post('/images', json=PydanticDocument().json(), headers={"Content-Type": "application/json"})
print(response, response.text)