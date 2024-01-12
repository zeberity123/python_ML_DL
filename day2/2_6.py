# numpy.py
import numpy as np
a = list('abcdefg')
print(a)
print(a[0], a[-1])
print(a[:3])
print(a[3:])
print(a[::2])
print('-'*30)

b = np.arange(12)
print(b)
print(type(b))
print(b.shape, b.dtype, b.size)
print(b+1)
print(b+b) # vector
print(np.sin(b)) # universal function
print(sum(b))
print('-'*30)

c = b.reshape(3, 4)

print(c)
print(c+1)
print(c+c)
print(np.sin(c))
print(np.cos(c))

d = b.reshape(3, 4)
d = b.reshape(3, -1)
d = b.reshape(-1, 4)
print(d)

# 2차원 배열을 1차원으로 변환
w = np.arange(4)
w = w.reshape(2, 2)
print(w, w.shape)
print('----------------')
print(w.reshape(12))
print(w.reshape(w.size))
print(w.reshape(-1))
