from math import floor, sqrt


def soma(x):
    s = 0
    for i in x:
        s += i
    return s


def media(x):
    return soma(x) / len(x)


def mediana(x):
    x.sort()
    n = len(x) // 2
    if len(x) % 2 == 0:
        return media(x[n-1:n+1])
    else:
        return x[n]


def moda(x):
    return max(x, key=x.count)


def variancia(x):
    n = len(x)
    return (1 / (n - 1)) * (soma([i**2 for i in x]) - ((soma(x)**2) / n))


def desvio_padrao(x):
    return sqrt(variancia(x))


def percentil(x, k):
    x = x.sort()
    h = (len(x) - 1) * k + 1
    p = x[floor(h)] + ((h - floor(h)) * (x[floor(h) + 1] - x[floor(h)]))
    return p


def lim_inferior(x):
    li = percentil(x, 0.25) - 1.5 * (percentil(x, 0.75) - percentil(x, 0.25))
    return [i for i in x if x < li][0]


def lim_superior(x):
    ls = percentil(x, 0.75) + 1.5 * (percentil(x, 0.75) - percentil(x, 0.25))
    return [i for i in x if x > ls][0]


def amplitude(x):
    return max(x) - min(x)


def coeficiente_variacao(x):
    return (desvio_padrao(x) / media(x)) * 100


def momento(x, k):
    n = len(x)
    return (1 / (n - 1)) * (soma([(i - media(x)) ** k for i in x]))


def assimetria(x):
    return (momento(x, 3)) / (sqrt(momento(x, 2)) ** 3)


def curtose(x):
    return (momento(x, 4)) / (sqrt(momento(x, 2)) ** 4)
