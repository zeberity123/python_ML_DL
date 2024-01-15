# 3_2_kma.py
import re
import requests


f = open('data/kma.csv', 'w', encoding='utf-8')

# 퀴즈
# 기상청 주소로부터 province 데이터만 읽어오세요
url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
response = requests.get(url)
# print(response.text)

# print(re.findall(r'<province>(.+)</province>', response.text))

# 퀴즈
# location을 찾아보세요
# DOTALL: 여러 줄에 걸쳐있을 때 사용(개행문자를 무시)
# .+: 탐욕적(greedy)
# .+?: 비탐욕적(non-greedy)
locations = re.findall(r'<location wl_ver="3">(.+?)</location>',
                       response.text, re.DOTALL)
# print(len(locations))

# province를 찾아보세요
# city를 찾아보세요
for loc in locations:
    # print(loc)
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], city[0])

    # 퀴즈
    # province와 city를 한번에 찾아보세요
    # pv = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', loc, re.DOTALL)
    # pv = re.findall(r'<province>(.+)</province>\s+<city>(.+)</city>', loc)
    # print(pv[0])

    # 퀴즈
    # data를 찾아보세요
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(len(data))

    # 퀴즈
    # data 안에 포함된 mode, tmEf, wf, tmn, tmx, rnSt를 찾아보세요
    for datum in data:
        mode = re.findall(r'<mode>(.+)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+)</wf>', datum)
        tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        # print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0])
        # print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0],
        #       file=f, sep=',')

        f.write('{},{},{},{},{},{},{},{}\n'.format(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0]))

        # 퀴즈
        # mode 등등을 한번에 찾아보세요
        # items = re.findall(r'<[A-Za-z]+>(.+)</[A-Za-z]+>', datum)
        # items = re.findall(r'<\w+>(.+)</\w+>', datum)
        # items = re.findall(r'<.+>(.+)</.+>', datum)
        # items = re.findall(r'>(.+)<', datum)
        # print(items)

f.close()

# 퀴즈
# 앞에서 출력한 내용으로 kma.csv 파일을 만드세요


