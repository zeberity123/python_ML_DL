import re
import requests
from bs4 import BeautifulSoup

w = '하늘'
url = f'http://openhangul.com/nlp_ko2en?q={w}'

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
data = soup.find_all(attrs={"class": "console"}).__str__()
word = re.findall(r'br/>[A-z]+', data)[0][4:]

print(f'{w} ==> {word}')
