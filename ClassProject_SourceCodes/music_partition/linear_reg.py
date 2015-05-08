
import matplotlib.pyplot as plt
import pylab
from common import node_color,data_count_import


def linear_reg_plotter(group,x,y):

    plt.axes(axisbg="#777777")
    fit = pylab.polyfit(x,y,1)
    fit_fn = pylab.poly1d(fit)
    plt.scatter(x,y,color=node_color[group])

    plt.plot(x, fit_fn(x),color=node_color[group])


def main():
    data = data_count_import("count.txt")
    group = set([g for g,t_ID,play,like in data])

    for e in group:
        x_and_y = [(play,like) for g,t_ID,play,like in data if g == e ]
        linear_reg_plotter(e,*zip(*x_and_y))

    plt.xlim(0,0.5*10**8)
    plt.ylim(0,7*10**5)
    plt.xlabel("play counts")
    plt.ylabel("number of likes")
    plt.show()

if __name__ == '__main__':
    main()