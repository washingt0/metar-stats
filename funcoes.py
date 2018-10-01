def soma(x):
    sum = 0
    for i in x:
        sum += i

    return sum

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
    pass

def desvio_padra(x):
    pass

def percentil(x, k):
    pass

def quartil(x, k):
    pass

def coef_variacao(x):
    pass
