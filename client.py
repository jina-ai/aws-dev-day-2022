import requests
from docarray import DocumentArray
import json

da_name = 'aws_china_dev_day_demo_202208_cn_alpha'
# images = load_data(da_name)


# url = 'http://localhost:8000/images/'

url = 'http://52.81.237.209:45678/images'

# x = requests.post(url, data=json.dumps(images[0].to_dict()),
#                   headers={"Content-Type": "application/json", "accept": "application/json"})
#
# print(x)
# print(x.text)

x = requests.get(url,
                 params={'skip': 0, 'limit': 1},
                 headers={"Content-Type": "application/json", "accept": "application/json"})
from docarray.document.pydantic_model import PydanticDocumentArray
resp = x.json()
da = DocumentArray.from_list(resp)
print(da.summary())
