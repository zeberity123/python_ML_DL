import random


def f_2(a=0, b=0, c=0):
    print(a, b, c)


f_2()
f_2(3)
f_2(3, 9)
f_2(3, 9, 3)
f_2(b=3, c=9)

a = [random.randrange(100) for _ in range(10)]
print(a)
print(a[::-1])
print([a[i] for i in range(len(a)-1, -1, -1)])
print(list(reversed(a)))

print(list(filter(lambda x: x % 2, a)))
# print([i for i in a if i % 2])

n = 3
m = 9
print(n, m)
n, m = m, n
print(n, m)


def to_lower(s):
    return s.lower()


colors = ['red', 'green', 'YELLOW', 'blue']
print(sorted(colors))
print(sorted(colors, key=to_lower))
print(sorted(colors, key=to_lower, reverse=True))
print(sorted(colors, key=len))

print(sum([str(i).count('8') for i in range(10001)]))
print(len([c for i in range(10000) for c in str(i) if c == '8']))
print(str(list(range(10000))).count('8'))

n = 0
for i in range(10000):
    for c in str(i):
        n += c == '8'
print(n)
