# 3_1_open_hangul.py
import re
import requests


# 퀴즈
# 오픈한글 사이트에서 한글 자판을 알파벳 자판으로 바꿔주는 서비스를 사용해서
# 특정 단어를 변환하는 코드를 만드세요
def convert(hangul):
    url = 'http://openhangul.com/nlp_ko2en?q=' + hangul
    response = requests.get(url)
    # print(response)
    # print(response.text)
    # print(response.content)

    text = response.content.decode('utf-8')
    # print(text)

    # alpha = re.findall(r'<img src="images/cursor.gif"><br>([a-z]+)', text)
    alpha = re.findall(r'<img src="images/cursor.gif"><br>(.+)', text)
    return alpha[0]


# 퀴즈
# 내가 입력한 단어에 대해 변환해주는 함수를 만드세요
print(convert('하늘'))
print(convert('사랑은 남아'))
print(convert('점심'))
print(convert('김치찌개'))
print(convert('컴퓨터'))



