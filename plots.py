import matplotlib.pyplot as plt
import time


def plot_save_histogram(data):
    name = str(time.time()).replace('.', '') + '.png'
    plt.clf()
    plt.hist(data, bins='auto')
    plt.savefig(name)
    return name
