import matplotlib.pyplot as plt
import numpy as np

def plot_equation(equation, root, start, end):
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

    x = np.arange(start - 2, end + 2, 0.01)

    plt.plot([i for i in x], [equation(i) for i in x])

    plt.plot(root, equation(root), marker='o', markerfacecolor="orange")

    ax.grid(which='major', color='#bbb', linewidth=0.8)
    ax.minorticks_on()
    ax.set_xlabel('x-axis', color='white')
    ax.set_ylabel('y-axis', color='white')

    return fig


def plot_system(equation1, equation2, root1, root2):
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

    delta = 0.01
    xrange = np.arange(root1 - 2, root1 + 2, delta)
    yrange = np.arange(root2 - 2, root2 + 2, delta)
    X, Y = np.meshgrid(xrange, yrange)

    F = equation1(X, Y)
    G = equation2(X, Y)

    plt.contour(X, Y, F, [0], colors=['green'])
    plt.contour(X, Y, G, [0], colors=['red'])

    ax.grid(which='major', color='#bbb', linewidth=0.8)
    ax.minorticks_on()
    ax.set_xlabel('x-axis', color='white')
    ax.set_ylabel('y-axis', color='white')

    return fig

