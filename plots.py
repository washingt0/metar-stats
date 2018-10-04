import matplotlib.pyplot as plt
import time
import numpy as np


def plot_save_histogram(data):
    name = str(time.time()).replace('.', '') + '.png'
    plt.clf()
    plt.hist(data, bins='auto')
    plt.savefig(name)
    return name


def plot_save_regression(data, t=1):
    name = str(time.time()).replace('.', '') + '.png'
    plt.clf()
    x = np.array([i for i in range(1, len(data)+1)])
    data = np.array(data)
    ca, cb = np.polyfit(x, data, 1)
    plt.plot(x, data, 'yo', x, ca*x+cb, '--k')
    plt.plot(x, data)
    if t == 1:
        a, b, = 10, 50
    elif t == 2:
        a, b = 0, 25
    elif t == 3:
        a, b = 1000, 1050
    plt.xlim(0, len(data)+1)
    plt.ylim(a, b)
    plt.savefig(name)
    return {
        "nome": name,
        "coef_a": ca,
        "coef_b": cb
    }

