# 1_3_file.py

# 퀴즈
# poem.txt 파일에 들어있는 단어 갯수를 알려주세요
f = open('data/poem.txt', 'r', encoding='utf-8')         # euc-kr

words = 0
for line in f:
    print(line.strip().split())
    words += len(line.strip().split())

f.close()

print('단어 : {}'.format(words))




