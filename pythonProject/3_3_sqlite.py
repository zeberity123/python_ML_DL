# 3_3_sqlite.py
import sqlite3

# CRUD: Create, Read, Update, Delete


# 퀴즈
# kma.csv 파일을 2차원 리스트로 반환하는 함수를 만드세요
def read_kma():
    # with open('data/kma.csv', 'r', encoding='utf-8') as f:
    #     rows = []
    #     for line in f:
    #         rows.append(line.strip().split(','))
    #
    # return rows

    with open('data/kma.csv', 'r', encoding='utf-8') as f:
        return [line.strip().split(',') for line in f]


def create_db():
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    cursor.execute(query)

    conn.commit()
    conn.close()


def insert_row(row):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    # 퀴즈
    # row에 들어있는 데이터를 전달하세요
    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cursor.execute(query)

    conn.commit()
    conn.close()


# 퀴즈
# insert_all 함수를 만드세요
def insert_all(rows):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for row in rows:
        query = base.format(*row)
        cursor.execute(query)

    conn.commit()
    conn.close()


def fetch_all():
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    rows = []
    query = 'SELECT * FROM kma'
    for r in cursor.execute(query):
        rows.append(r)

    # conn.commit()
    conn.close()

    return rows


def search_city(city):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    rows = []
    query = 'SELECT * FROM kma WHERE city="{}"'.format(city)
    for r in cursor.execute(query):
        rows.append(r)

    # conn.commit()
    conn.close()

    return rows


# create_db()

# rows = read_kma()
# print(*rows, sep='\n')

# for row in rows:
#     insert_row(row)
# insert_all(rows)

# rows = fetch_all()
# print(*rows, sep='\n')

# 퀴즈
# 원하는 city의 날씨 데이터를 반환하는 함수를 만드세요
print(*search_city('이천'), sep='\n')
print(*search_city('군산'), sep='\n')




