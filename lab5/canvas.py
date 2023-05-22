import matplotlib.pyplot as plt
import numpy as np

def plot(lagrange, gaussian, x, y):
    fig = plt.figure()
    fig.patch.set_facecolor('#212121')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('#212121')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.xaxis.label.set_color('red')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(which='major', color='white', linewidth=1)
    space = np.arange(min(x),
                      max(x) + 0.01, 0.01)

    plt.plot([i for i in space], [lagrange(i) for i in space], label='lagrange', linewidth=1)
    plt.plot([i for i in space], [gaussian(i) for i in space], label='gaussian', linewidth=1)

    for i in range(len(x)):
        plt.plot(x[i], y[i], marker='o', markerfacecolor="white", linewidth=3)

    plt.legend()
    ax.grid(which='major', color='#bbb', linewidth=0.8)
    ax.minorticks_on()
    ax.set_xlabel('x-axis', color='white')
    ax.set_ylabel('y-axis', color='white')

    return fig
