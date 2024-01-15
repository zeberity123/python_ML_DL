# 2_4_numpy.py
import numpy as np

a = list('abcdefg')
print(a)

print(a[0], a[-1])
print(a[:3])
print(a[3:])
print(a[::2])
print('-' * 30)

b = np.arange(12)
# b = np.arange(0, 12)
# b = np.arange(0, 12, 1)
print(b)
print(type(b))          # <class 'numpy.ndarray'>
print(b.shape, b.dtype, b.size)

print(b + 1)            # broadcast
print(b * 3)
print(b > 5)
print(3 * b)
print(b + b)            # vector
print(np.sin(b))        # universal function
print(sum(b))
print('-' * 30)

c = b.reshape(3, 4)
print(c)

print(c + 1)            # broadcast
print(c + c)            # vector
print(np.sin(c))        # universal
print(np.cos(c))
print('-' * 30)

d = b.reshape(3, 4)
d = b.reshape(3, -1)
d = b.reshape(-1, 4)
print(d)

# 퀴즈
# 2차원 배열을 1차원으로 변환하세요 (3가지)
print(d.reshape(12))
print(d.reshape(d.size))
print(d.reshape(len(d) * len(d[0])))
print(d.reshape(-1))





