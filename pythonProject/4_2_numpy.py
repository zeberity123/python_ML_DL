# 4_2_numpy.py
import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

# 퀴즈
# 2차원 배열 마지막 요소를 출력해 보세요 (11)
print(a[-1])
print(a[-1, -1])                # fancy indexing

a[-1, -1] = 99

# 퀴즈
# 마지막 열만 출력해 보세요
print(a[-1])
print(a[-1, :])
print(a[:, -1])

print(a[-1:, :])
print(a[:, -1:])
print(a[:, -1].reshape(-1, 1))
print('-' * 30)

print(np.zeros(3))
print(np.zeros(3, dtype=np.int32))
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.full((3, 4), fill_value=-1))
print('-' * 30)

b = np.zeros((5, 5), dtype=np.int32)
print(b)

# 퀴즈
# 2차원 배열의 테두리를 1로 채워보세요
# b[0] = 1
# b[-1] = 1
# b[:, 0] = 1
# b[:, -1] = 1
b[[0, -1]] = 1
b[:, [0, -1]] = 1

# 퀴즈
# 2차원 배열의 속을 2로 채워보세요
b[1:-1, 1:-1] = 2

# 퀴즈
# 2차원 배열의 대각선을 3으로 채워보세요 (반복문 사용 안함)
# b[0, 0] = 3
# b[1, 1] = 3
# b[[0, 1], [0, 1]] = 3         # index array
b[range(5), range(5)] = 3

for i in range(len(b)):
    b[i, i] = 3

print(b)
print('-' * 30)

c1 = np.arange(12).reshape(3, 4)
c2 = np.arange(12).reshape(4, 3)

print(np.dot(c1, c2))

print(c1)
print(np.transpose(c1))

