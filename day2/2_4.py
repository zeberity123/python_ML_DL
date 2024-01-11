import requests
import re
import json

# url = 'https://www.naver.com/'
url = 'https://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
text = response.content.decode('utf-8')

data = json.loads(text)
# for i in data:
#     print(i['code'], i['value'])


# code = re.findall(r'[0-9]+', text)
code = re.findall(r'"code":"([0-9]+)"', text)

# value = re.findall(r'[가-힣]+', text)
value = re.findall(r'"value":"([가-힣]+)"', text)

# for i in range(len(code)):
#     print(f'{code[i]} -> {value[i]}')

# for c, v in zip(code, value):
#     print(c, v)

# findall 함수를 한 번만 사용
mix = re.findall(r'"code":"([0-9]+)","value":"([가-힣]+)"', text)
for i, j in mix:
    print(i, j)


