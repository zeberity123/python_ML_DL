import re
import requests
import json


def get_songs(code, page):
    payload = {
        'S_PAGENUMBER': page,
        'S_MB_CD': code
        # 'S_HNBA_GBN': 'I'
        # 'hanmb_nm': 'G-DRAGON',
        # 'soft_field': 'SORT_PBCTN_DAY'
    }

    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    response = requests.post(url, data=payload)
    tbody = re.findall(r'<tbody>(.+?)</tbody>', response.text, re.DOTALL)
    trs = re.findall(r'<tr>(.+?)</tr>', tbody[1], re.DOTALL)
    # for tr in trs:
    #     tds = re.findall(r'<td>(.*?)</td>', tr)
    #     print(tds)

    s_list = []
    for tr in trs:
        tr = tr.replace('<br/>', ',')
        tr = re.sub(r' <img .+? />', '', tr)
        tds = re.findall(r'<td>(.*?)</td>', tr)
        tds[0] = tds[0].strip()

        s_list.append(tds)

    return s_list


# 노래 목록
s_list = []
for i in range(1, 18):
    g_list = get_songs('W0726200', i)
    for j in g_list:
        s_list.append(j)

for i in s_list:
    print(i)

