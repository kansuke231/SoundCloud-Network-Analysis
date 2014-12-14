from __future__ import division
import matplotlib.pyplot as plt

def data_import(filename):

    i = 1
    result = []
    n = 0 # sum
    with open(filename,"r") as f:
        for e in f.readlines():
            result.append((i,int(e)))
            i+=1
            n+=int(e)
    return result,n

def plotter(data):

    plt.plot(*zip(*data))
    plt.yscale("log")
    plt.xscale("log")
    plt.ylabel("fraction of edges")
    plt.xlabel("weight")
    plt.grid(True,which='both')
    plt.show()

def main():

    data,n = data_import("track2_hist.txt")
    plotter([(i,e/n) for i,e in data])

if __name__ == "__main__":
    main()