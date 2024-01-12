import re
import requests


def convert(w):
    url = f'http://openhangul.com/nlp_ko2en?q={w}'

    response = requests.get(url)
    text = response.content.decode('utf-8')

    alpha = re.findall(r'<img src="images/cursor.gif"><br>(.+)', text)
    # print(alpha)
    return alpha[0]


print(convert('하늘'))


