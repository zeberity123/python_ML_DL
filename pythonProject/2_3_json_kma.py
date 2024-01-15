# 2_3_json_kma.py
import re

import requests
import json

# url = 'https://www.naver.com/'
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
print(response)
print(response.text)
print(response.content)

text = response.content.decode('utf-8')
print(text)
# [{"code":"11","value":"서울특별시"},{"code":"26","value":"부산광역시"},{"code":"27","value":"대구광역시"},{"code":"28","value":"인천광역시"},{"code":"29","value":"광주광역시"},{"code":"30","value":"대전광역시"},{"code":"31","value":"울산광역시"},{"code":"41","value":"경기도"},{"code":"42","value":"강원도"},{"code":"43","value":"충청북도"},{"code":"44","value":"충청남도"},{"code":"45","value":"전라북도"},{"code":"46","value":"전라남도"},{"code":"47","value":"경상북도"},{"code":"48","value":"경상남도"},{"code":"50","value":"제주특별자치도"}]

# 퀴즈
# 기상청에서 읽어온 데이터로부터 code와 value만 예쁘게 출력하세요 (json 사용)
# 11 서울특별시
# 26 부산광역시
items = json.loads(text)
# print(type(items))
for item in items:
    # print(item, type(item))
    # for k in item:
    #     print(item[k], end=' ')
    # print()

    print(item['code'], item['value'])
print('-' * 30)

# 퀴즈
# 기상청에서 읽어온 데이터로부터 code와 value만 예쁘게 출력하세요 (정규표현식 사용)
# codes = re.findall(r'[0-9]+', text)
# values = re.findall(r'[가-힣]+', text)

codes = re.findall(r'"code":"([0-9]+)"', text)
values = re.findall(r'"value":"([가-힣]+)"', text)
print(codes)
print(values)

for i in range(len(codes)):
    print(codes[i], values[i])
print()

for c, v in zip(codes, values):
    print(c, v)
print()

# 퀴즈
# findall 함수를 한 번만 사용해서 결과를 가져오세요
cv = re.findall(r'{"code":"([0-9]+)","value":"([가-힣]+)"}', text)
for c, v in cv:
    print(c, v)







