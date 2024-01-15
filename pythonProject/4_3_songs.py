# 4_3_songs.py
import re
import requests


# 퀴즈
# 한국음악저작권협회에서 지드래곤의 저작권 정보를 가져오세요
def get_songs(code, page):
    payload = {
        'S_PAGENUMBER': page,
        'S_MB_CD': code,
        # 'S_HNAB_GBN': 'I',
        # 'hanmb_nm': 'G-DRAGON',
        # 'sort_field': 'SORT_PBCTN_DAY',
    }

    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    response = requests.post(url, data=payload)
    # print(response)
    # print(response.text)

    # 퀴즈
    # 저작물 정보를 깔끔하게 출력하세요
    tbody = re.findall(r'<tbody>(.+?)</tbody>',
                       response.text, re.DOTALL)
    # print(len(tbody))
    # print(tbody[1])

    trs = re.findall(r'<tr>(.+?)</tr>', tbody[1], re.DOTALL)
    # print(len(trs))

    for tr in trs:
        # print(tr)
        tr = tr.replace('<br/>', ',')
        # tr = tr.replace(' <img src="/images/common/control.gif"  alt="" />', '')
        # tr = tr.replace(' <img src="/images/common/control.gif" alt="" />', '')
        tr = re.sub(r' <img .+? />', '', tr)

        tds = re.findall(r'<td>(.*?)</td>', tr)
        tds[0] = tds[0].strip()
        print(tds)

    return len(trs) > 0


# 퀴즈
# 앞에서 만든 코드를 함수로 바꾸고
# 지드래곤의 모든 노래를 가져와 보세요
page = 1
while get_songs(code='W0726200', page=page):
    print('-' * 10, page)
    page += 1
