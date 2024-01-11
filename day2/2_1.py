import csv
import re

# f = open('us-500.csv', 'r', encoding='utf-8')
# db = [list(eval(i.strip())) for i in f.readlines()][1:]
# f.close()
# print(*db[:5], sep='\n')
# for i, line in enumerate(f):
#     if i != 0:
#


def read_us500_2():
    f = open('us-500.csv', 'r', encoding='utf-8')
    rows = []
    f.readline()
    for items in csv.reader(f, delimiter=','):
        # print(items)
        rows.append(items)

    f.close()
    return rows


rows = read_us500_2()
print(*rows[:3], sep='\n')

