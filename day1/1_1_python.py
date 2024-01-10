# for _ in range(3): print('hello')
#
# print('\n')
#
# print('hello')
# print('hello')
# print('hello')
#
#
# print('\n')
#
# w = 0
# while (w<3):
#     print('hello')
#     w+=1
#
# print('\n')
#
# a = ['hello', 'hello', 'hello']
# print(a)
#
# s = 'hello '
# print(s * 3)

n = 5
rng = int((n/2)+1)
# for i in range(rng-1):
#     print(' ' * i, end='')
#     print('*', end='')
#     print(' ' * (rng - i*2), end='')
#     print('*')
# print(' '*(rng-1), end='')
# print('*')
# for i in range(rng-1, -1):
#     print(' ' * (rng - i * 2), end='')
#     print('*', end='')
#     print(' ' * i, end='')
#     print('*')

# for i in range(n):
#     for j in range(n):
#         if i == j or i+j == 4:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#

for i in range(n):
    for j in range(n):
        if i % n-1 == 0 or j % n-1 == 0:
            print('*', end='')
        else: print(' ', end='')
    print()