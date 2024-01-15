# 4_1_matplotlib.py
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import colors, colormaps

plt.rcParams['font.family'] ='Malgun Gothic'


def p4():
    # 퀴즈
    # 100보다 작은 난수 100개로 구성된 x, y를 만드세요
    x = [random.randrange(100) for _ in range(100)]
    y = [random.randrange(100) for _ in range(100)]

    plt.subplot2grid(shape=(3, 4), loc=(1, 1), rowspan=2)
    plt.plot(x, y, 'r>')

    # 퀴즈
    # subplot2grid 함수를 여러 번 사용해서 빈 곳을 모두 채워보세요
    plt.subplot2grid(shape=(3, 4), loc=(0, 0), rowspan=3)
    plt.plot(x, y, 'go')

    plt.subplot2grid(shape=(3, 4), loc=(0, 1), colspan=3)
    plt.plot(x, y, 'k')

    plt.subplot2grid(shape=(3, 4), loc=(1, 2), colspan=2, rowspan=2)
    # plt.plot(x, y, 'yx')
    plt.scatter(x, y, s=3)

    plt.show()


def p5():
    males = [30, 35, 27, 31, 37]
    females = [29, 36, 37, 42, 19]

    # 퀴즈
    # females 그래프를 추가하세요
    # idx_m = range(0, len(males)*2, 2)
    # idx_f = range(1, len(males)*2, 2)
    #
    # plt.bar(idx_m, males, width=0.9)
    # plt.bar(idx_f, females, width=0.9)

    idx = np.arange(len(males))

    plt.bar(idx, males, width=0.45)
    plt.bar(idx+0.5, females, width=0.45)
    plt.show()


# 퀴즈
# 2016_GDP.txt 파일을 읽고 top10을 막대 그래프로 그려보세요
def get_top10():
    f = open('data/2016_GDP.txt', 'r', encoding='utf-8')

    f.readline()

    names, dollars = [], []
    for line in f:
        # print(line.strip().split(':'))
        _, n, d = line.strip().split(':')

        names.append(n)
        dollars.append(int(d.replace(',', '')))

    f.close()
    return names[:10], dollars[:10]


def p6():
    n10, d10 = get_top10()
    print(n10)
    print(d10)

    idx = range(len(n10))
    # plt.bar(idx, d10)
    # plt.bar(idx, d10, color=['red', 'green', 'blue'])
    # plt.bar(idx, d10, color=['DeepSkyBlue', 'MediumOrchid', 'Coral'])
    # plt.bar(idx, d10, color=colors.BASE_COLORS)
    plt.bar(idx, d10, color=colors.TABLEAU_COLORS)

    # 퀴즈
    # 한글이 안깨지도록 처리하세요
    plt.xticks(idx, n10, rotation=45)
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.title('2016 GDP Top10')
    plt.show()


def p7():
    # 퀴즈
    # x 모양의 scatter 그래프를 그려보세요
    x = np.arange(100)

    plt.subplot(2, 2, 1)
    plt.scatter(x, x, s=5, c=x)
    plt.scatter(x[::-1], x, s=5, c=x)

    plt.subplot(2, 2, 2)
    plt.scatter(x, x, s=5, c=x, cmap='jet')
    plt.scatter(x[::-1], x, s=5, c=x, cmap='jet_r')

    plt.subplot(2, 2, 3)
    plt.scatter(x, x, s=5, c=x, cmap='pink')
    plt.scatter(x[::-1], x, s=5, c=x, cmap='prism')

    plt.show()


def p8():
    v = colormaps.get_cmap('viridis')
    print(v)

    print(v(-1))
    print(v(0))
    print(v(255))
    print(v(256))

    print(v(1.0))
    print(v(0.5))
    print(v(127/255))
    print(v(128/255))


# p4()
# p5()
# p6()
# p7()
p8()

# print(list(colormaps))
# ['magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 'twilight_shifted',
# 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd',
# 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy',
# 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr',
# 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm',
# 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar',
# 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv',
# 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring',
# 'summer', 'terrain', 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1',
# 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'grey', 'gist_grey', 'gist_yerg',
# 'Grays', 'magma_r', 'inferno_r', 'plasma_r', 'viridis_r', 'cividis_r', 'twilight_r',
# 'twilight_shifted_r', 'turbo_r', 'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r',
# 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r',
# 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 'RdYlBu_r',
# 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r', 'YlGnBu_r', 'YlOrBr_r',
# 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r',
# 'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r',
# 'gist_heat_r', 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r',
# 'gnuplot_r', 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r',
# 'ocean_r', 'pink_r', 'prism_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r',
# 'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r', 'Paired_r', 'Pastel1_r', 'Pastel2_r',
# 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r', 'tab20b_r', 'tab20c_r']
