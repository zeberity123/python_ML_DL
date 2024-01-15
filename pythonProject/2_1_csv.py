# 2_1_csv.py
import csv


# 퀴즈
# us-500.csv 파일을 읽어서 2차원 리스트로 반환하는 함수를 만드세요
# "James","Butt","Benton, John B Jr","6649 N Blue Gum St","New Orleans","Orleans","LA",70116,"504-621-8927","504-845-1427","jbutt@gmail.com","http://www.bentonjohnbjr.com"
# "Josephine","Darakjy","Chanay, Jeffrey A Esq","4 B Blue Ridge Blvd","Brighton","Livingston","MI",48116,"810-292-9388","810-374-9840","josephine_darakjy@darakjy.org","http://www.chanayjeffreyaesq.com"
# [["James","Butt","Benton, John B Jr", ...],
#  ["Josephine","Darakjy","Chanay, Jeffrey A Esq", ...]]
def read_us500_1():
    f = open('data/us-500.csv', 'r', encoding='utf-8')

    # rows = []
    # for i, line in enumerate(f):
    #     if i != 0:
    #         # print(eval(line.strip()))
    #         rows.append(list(eval(line.strip())))

    f.readline()        # skip header
    # for line in f:
    #     rows.append(list(eval(line.strip())))

    rows = [list(eval(line.strip())) for line in f]
    f.close()
    return rows


def read_us500_2():
    f = open('data/us-500.csv', 'r', encoding='utf-8')

    rows = []

    f.readline()
    for items in csv.reader(f, delimiter=','):
        rows.append(items)

    f.close()
    return rows


def read_us500_3():
    f = open('data/us-500.csv', 'r', encoding='utf-8')
    f.readline()

    rows = []
    for line in f:
        it = iter(line.strip().split(','))
        items = []
        for col in it:
            n = col.count('"')
            if n == 0:
                items.append(str(col))
            elif n == 1:
                next_col = next(it)
                items.append(col[1:] + ',' + next_col[:-1])
            else:
                items.append(col[1:-1])

        rows.append(items)

    # rows = []
    # for line in f:
    #     it = iter(line.strip().split(','))
    #     items = []
    #     for col in it:
    #         n = col.count('"')
    #         if n == 0:
    #             items.append(str(col))
    #         elif n == 1:
    #             next_col = next(it)
    #             items.append(col[1:] + ',' + next_col[:-1])
    #         else:
    #             items.append(col[1:-1])
    #
    #     rows.append(items)

    f.close()
    return rows


def read_us500_4():
    f = open('data/us-500.csv', 'r', encoding='utf-8')
    f.readline()

    rows = []
    first = True
    for line in f:
        col = ''
        items = []
        for c in line.strip():
            if c == '"':
                if first:
                    first = False
                else:
                    first = True
            elif c == ',':
                if first:
                    if col:
                        items.append(col)
                        col = ''
                    else:
                        items.append('')
                else:
                    col += c
            else:
                col += c

        items.append(col)
        rows.append(items)

    f.close()
    return rows


rows = read_us500_4()
print(*rows[:3], sep='\n')

# csv.writer()

