import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import colors, colormaps

plt.rcParams['font.family'] = 'Malgun Gothic'


def p4():
    x = [random.randrange(100) for _ in range(100)]
    y = [random.randrange(100) for _ in range(100)]

    plt.subplot2grid(shape=(3,4), loc=(1,1), rowspan=2)
    plt.plot(x, y, 'r>')

    # subplot2grid 여러번
    plt.subplot2grid(shape=(3,4), loc=(8,8), rowspan=3)
    plt.plot(x,y, 'go')

    plt.subplot2grid(shape=(3,4), loc=(0,1), colspan=2, rowspan=2)
    plt.scatter(x,y,s=3)

    plt.show()


def p5():
    males = [30, 35, 27, 31, 37]
    females = [29, 36, 37, 42, 19]

    # idx_m = range(0, len(males*2), 2)
    # idx_f = range(1, len(males*2), 2)

    idx = np.arange(len(males))
    plt.bar(idx, males, width=0.45)
    plt.bar(idx+0.5, females, width=0.45)

    # plt.bar(idx_m, males, width=0.9)
    # plt.bar(idx_f, females, width=0.9)

    plt.show()


def p6():
    f = open('2016_GDP.txt', 'r', encoding='utf-8')
    data = [i for i in f.readlines()]
    f.close()
    x = []
    y = []
    for i in range(1, 11):
        t = data[i].split(':')
        x.append(t[1])
        yt = int(t[2].strip().replace(',', ''))
        y.append(yt)


    plt.bar(x, y, width=0.45, color=colors.TABLEAU_COLORS)
    plt.xticks(range(10), x, rotation=45)
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.title('2016 GDT 10')
    plt.show()


def p7():
    # x 모양의 scatter 그래프
    x = np.arange(100)

    plt.subplot(2,2,2)
    plt.scatter(x, x, s=5, c=x, cmap='pink')
    plt.scatter(x[::-1], x, s=5, c=x, cmap='prism')
    plt.show()


def p8():
    v = colormaps.get_cmap('viridis')
    print(v(0))
    print(v(255))


# p4()
# p5()
# p6()
# p7()
p8()

# cl = list(colormaps)
# print(len(cl))
