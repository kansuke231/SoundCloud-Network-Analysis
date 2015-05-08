
import matplotlib.pyplot as plt
from common import node_color,data_count_import


def plotter(x,y,g):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    labels = x
    x = [e for e in range(len(x))]
    print(x)
    print(y)
    print(g)
    bars = ax1.bar(x,y)
    plt.ylabel("play count")
    plt.xlabel("rank")
    for e in x:
        bars[e].set_facecolor(node_color[g[e]])

    #plt.xticks(x,labels,rotation='vertical')

    plt.show()

def main():
    data = data_count_import("count.txt")
    play_counts = sorted([(t_ID,play,g) for g,t_ID,play,like in data],
                         key=lambda x:x[1],reverse=True)

    plotter(*zip(*play_counts))

if __name__ == "__main__":
    main()