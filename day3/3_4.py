import matplotlib.pyplot as plt
import numpy as np
import math

x = [i for i in range(-10, 11)]


def p1():
    y = x
    plt.plot(x, y, 'r')
    plt.plot(x, y, 'go')
    plt.show()


def p2():
    y = [i**2 for i in x]
    plt.plot(x, y, 'r')
    plt.plot(x, y, 'go')
    plt.show()


def p3():
    x = np.arange(0.1, 2, 0.1)

    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))
    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))
    plt.show()

# p1()
# p2()
p3()