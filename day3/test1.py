# 192.168.0.96
import requests
import json
import re
import time

url = 'https://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
text = response.content.decode('utf-8')

db = json.loads(text)
for i in db:
    print(i['code'], i['value'])

print('--------------------------')

data = re.findall(r'"code":"([0-9]+)","value":"([가-힣]+)"', text)
for c, v in data:
    print(c, v)

# w = []
# st = time.time()
# for i in range(10000):
#     for j in range(10000):
#         w.append(i+j)
# print(w.__sizeof__)
# print(sum(w))
# et = time.time()
# print(et-st)

