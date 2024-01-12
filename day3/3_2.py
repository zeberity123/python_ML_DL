# 기상청 주소로부터 province 데이터만 읽기
import requests
import re
import pandas as pd

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

response = requests.get(url)
text = response.content.decode('utf-8')


def convert1():
    return re.findall(r'<province>(.+)</province>', text)


def convert2():
    # DOTALL: 여러 줄에 걸쳐있을 때 사용(개행문자를 무시)
    # .+ : 탐욕적(greedy)
    # .+?: 비탐욕적(non-greedy)

    return re.findall(r'<location wl_ver="3">(.+?)</location>', text, re.DOTALL)


def convert3():
    data = convert2()
    province = []
    city = []
    for i in data:
        province.append(re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', i, re.DOTALL))
        city.append(re.findall(r'<city>(.+)</city>', i))
    return data, province, city


#

def convert4():
    data = convert2()
    data1 = []
    for i in data:
        data1.append(re.findall(r'<data>(.+?)</data>', i, re.DOTALL))
    r_data = []
    for j in data1:
        # r_data.append(re.findall(r'<mode>(.+)</mode>.+'
        #                          r'<tmEf>(.+)</tmEf>.+'
        #                          r'<wf>(.+)</wf>.+'
        #                          r'<tmn>(.+)</tmn>.+'
        #                          r'<tmx>(.+)</tmx>.+'
        #                          r'<rnSt>(.+)</rnSt>', j[0], re.DOTALL))

        # r_data.append(re.findall(r'<.+>(.+)</.+>', j[0]))
        r_data.append(re.findall(r'>(.+)<', j[0]))

    return r_data


# data1 = list(dict.fromkeys(convert1()))
# print(data1)
#
# data2 = convert2()
# print(len(data2))

data3 = convert3()
for i in range(41):
    print(data3[1][i])

data4 = convert4()
# for i in range(41):

# for i in range(len(data4)):
#     print(*data3[1][i][0], *data4[i])

# kma.csv 만들기
data = []
for i in range(len(data4)):
    data.append([*data3[1][i][0], *data4[i]])
# print(data)


df_list = ['province', 'city', 'mode', 'time', 'wf', 'tmn', 'tmx', 'rnSt']
df = pd.DataFrame(columns=df_list)


for i in range(len(data)):
    df.loc[i] = data[i]

print(df)
df.to_csv('kms1.csv', header=False, index=False)
# f = open('kms.csv', 'w', encoding='utf-8')
# f.write(''.format())
