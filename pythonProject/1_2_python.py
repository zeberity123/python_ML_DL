# 1_2_python.py
import random


def f_1(a, b, c):
    print(a, b, c)


f_1(1, 2, 3)        # positional
f_1(a=1, b=2, c=3)  # keyword
f_1(c=3, a=1, b=2)
# f_1(a=1, 2, c=3)


def f_2(a=0, b=0, c=0):
    print(a, b, c)


# 퀴즈
# f_2를 5가지 방식으로 호출해 보세요
f_2()
f_2(1)
f_2(1, 2)
f_2(1, 2, 3)
f_2(1)
f_2(c=1)
f_2(a=1, c=3)
f_2(1, c=3)

# help(print)


# 퀴즈
# 0~100 사이의 난수 10개로 이루어진 리스트를 만드세요
random.seed(41)

a = []
for _ in range(10):
    a.append(random.randrange(100))

print(a)

# 리스트를 만드는 한 줄짜리 반복문
b = [random.randrange(100) for _ in range(10)]
print(b)

# 퀴즈
# 리스트 b를 거꾸로 출력하세요 (3가지)
print(*b[::-1])

for i in range(len(b)-1, -1, -1):
    print(b[i], end=' ')
print()

for i in reversed(range(len(b))):
    print(b[i], end=' ')
print()

for i in reversed(b):
    print(i, end=' ')
print()

print(*[b[i] for i in reversed(range(len(b)))])

b.reverse()
print(*b)

n, m = 3, 8
print(n, m)

n, m = m, n
print(n, m)

k = m, n
print(k, k[0], k[1])

n, m = k
print(n, m)

t = 1, 3, 5
print(t, sep=',')
print(*t, sep=',')
print('-' * 30)

print(b)

# 퀴즈
# 리스트 b에서 홀수만 출력하세요
for i in b:
    if i % 2:
        print(i)

print([i for i in b if i % 2])
print('-' * 30)


def to_lower(s):
    return s.lower()


colors = ['red', 'green', 'YELLOW', 'blue']
print(sorted(colors))
print(sorted(colors, key=to_lower))
print(sorted(colors, key=to_lower, reverse=True))


# 퀴즈
# colors를 글자 갯수순으로 정렬하세요
def str_len(s):
    return len(s)


print(sorted(colors, key=str_len))
print(sorted(colors, key=lambda s: len(s)))
print(sorted(colors, key=len))

# 퀴즈
# 10000보다 작은 양수에 포함된 8의 갯수는?
# 808 : 2
# for i in range(100):
#     for c in str(i):
#         if c == '8':
#             print(c)
#
# w = [c for i in range(100) for c in str(i) if c == '8']
# print(w)
# print(len(w))
print(len([c for i in range(10000) for c in str(i) if c == '8']))

print('808'.count('8'))
print([str(i) for i in range(10)])
print([str(i).count('8') for i in range(10)])
print(sum([str(i).count('8') for i in range(10000)]))
print(str(list(range(10000))).count('8'))

n = 0
for i in range(10000):
    for c in str(i):
        n += (c == '8')

print(n)

