import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def data_import_edge(file_name):
    # input -> the name of the data file
    # output -> an edge list

    edge_list = []

    with open(file_name,"r") as f:
        for e in f.readlines():
            e = e.replace("\n","") # 1 23\n -> 1 23
            e = e.split(" ") # "1 23" -> ["1","23"]
            edge_list.append((int(e[0]),str(e[1])))

    return edge_list

def plotter(hist):
    data = [e for e in zip(hist[1],hist[0])]
    plt.plot(*zip(*data))
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("number of likes")
    plt.ylabel("frequency")
    plt.show()



edges = data_import_edge("user_to_tracks.txt")

G = nx.Graph()
G.add_edges_from(edges)

deg_dist = []

nodes = G.nodes()
for n in nodes:
    if type(n) == type(1):
        deg_dist.append(nx.degree(G,n))

deg_dist = sorted(deg_dist)


bins = [e for e in range(1,deg_dist[-1]+1)]
hist = np.histogram(deg_dist,bins=bins)
plotter(hist)
