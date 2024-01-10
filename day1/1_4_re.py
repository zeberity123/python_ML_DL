import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

print(db)
print(re.findall(r'[0-9]', db))

colors = ['red', 'green', 'YELLOW', 'blue']
print(sorted(colors, key=len))
print(str(list(range(10000))).count('8'))
print(sum([len(i.split(' '))for i in open('poem.txt', 'r', encoding='utf-8').readlines()]))

