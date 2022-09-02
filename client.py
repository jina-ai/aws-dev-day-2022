import requests
from docarray import DocumentArray
import json

da_name = 'aws_china_dev_day_demo_202208_cn_alpha'
# images = load_data(da_name)


# url = 'http://127.0.0.1:8000'

url = 'http://52.81.237.209:45678'

# x = requests.post(url, data=json.dumps(images[0].to_dict()),
#                   headers={"Content-Type": "application/json", "accept": "application/json"})
#
# print(x)
# print(x.text)

x = requests.get(f'{url}/images',
                 params={'skip': 0, 'limit': 100},
                 headers={"Content-Type": "application/json", "accept": "application/json"})
from docarray.document.pydantic_model import PydanticDocumentArray
resp = x.json()
da = DocumentArray.from_list(resp)
print(da.summary())

# resp = requests.get(
#     f'{url}/image_ids',
#     headers={"Content-Type": "application/json", "accept": "application/json"})
# print(resp)
# print(resp.json()['total_images'])
