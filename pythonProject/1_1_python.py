# 1_1_python.py

# ctrl + shift + f10

# 퀴즈
# hello를 3번 출력하는 코드를 5개 만드세요
print('hello', 'hello', 'hello')
print('hello' 'hello' 'hello')

print('hello hello hello')

print('hello')
print('hello')
print('hello')

print('hello' * 3)
print('hello', 'hello', sep='hello')

# alt + 1
# alt + 4


#   01234
# 0 *   * (0, 4)
# 1  * *  (1, 3)
# 2   *   (2, 2)
# 3  * *  (3, 1)
# 4 *   * (4, 0)
for i in range(5):
    for j in range(5):
        if i == j or i+j == 4:
            print('*', end='')
        else:
            print('-', end='')
    print()
print()

#   01234
# 0 *****
# 1 *   *
# 2 *   *
# 3 *   *
# 4 *****
for i in range(5):
    for j in range(5):
        # if i % 4 == 0 or j % 4 == 0:
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end='')
        else:
            print('-', end='')
    print()
print()



