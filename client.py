import requests
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

x = requests.get(url, headers={"Content-Type": "application/json", "accept": "application/json"})
resp = x.json()
print(type(resp))
print(resp['images'][0].keys())
# print(resp)
