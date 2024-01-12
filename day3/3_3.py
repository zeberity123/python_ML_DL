import sqlite3

# kma.csv 파일을 2차원 리스트로 변환하는 함수


def csv_to_2d(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for i in f.readlines():
            data.append(i.strip().split(','))
        return data


df_list = ['prov', 'city', 'mode', 'time', 'wf', 'tmn', 'tmx', 'rnSt']


def create_db():
    conn = sqlite3.connect('kms1.sqlite3')
    cursor = conn.cursor()
    # query = 'CREATE TABLE db_list (id INTEGER, name VARCHAR(16))'
    query = 'CREATE TABLE kms (prov TEXT, city TEXT, mode TEXT, time TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    cursor.execute(query)

    conn.commit()
    conn.close()


def insert_row(r):
    conn = sqlite3.connect('kms1.sqlite3')
    cursor = conn.cursor()

    query = 'INSERT INTO kms VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    base = query.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
    cursor.execute(base)

    conn.commit()
    conn.close()


def fetch_all():
    conn = sqlite3.connect('kms1.sqlite3')
    cursor = conn.cursor()
    rows = []
    query = 'select * from kms'
    for r in cursor.execute(query):
        rows.append(r)

    conn.commit()
    conn.close()

    return rows


def insert_all(rows):
    conn = sqlite3.connect('kms1.sqlite3')
    cursor = conn.cursor()

    base = 'INSERT INTO kms VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for r in rows:
        base = base.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
        cursor.execute(base)

    conn.commit()
    conn.close()

def search_city(city):
    conn = sqlite3.connect('kms1.sqlite3')
    cursor = conn.cursor()
    ans = []
    query = f'select * from kms where city = "{city}"'
    for r in cursor.execute(query):
        ans.append(r)

    conn.commit()
    conn.close()

    return ans

# create_db()
# rows = csv_to_2d('kms1.csv')
# # insert_all(rows)
# for row in rows:
#     insert_row(row)

# data = fetch_all()
# print(*data, sep='\n')

# 원하는 city의 날씨 데이터 가져오기
city_name = '대구'
c1 = search_city(city_name)
print(*c1, sep='\n')

