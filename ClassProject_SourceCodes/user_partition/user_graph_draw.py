import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

def data_import(file_name):
    # input -> the name of the data file
    # output -> an edge list

    edge_list = []

    with open(file_name,"r") as f:
        for e in f.readlines():
            e = e.replace(" ",",").replace("\n","")
            i,j,w = e.split(",") # "1,23" -> ["1","23"]
            edge_list.append((str(i),str(j),int(w)))

    return edge_list

def extractor(G,t):
    # input -> a graph G and an int t
    # output -> a list of edges whose weight is t
    return [(i,j) for i,j,attr in G.edges_iter(data=True) if attr["weight"] == t]

def min_or_max(G,func=max):
    return func([attr["weight"] for i,j,attr in G.edges_iter(data=True)])

def graph_draw(G):

    pos = nx.spring_layout(G)

    minimum = min_or_max(G,min) # the minimum of weights
    maximum = min_or_max(G,max)# the maximum of weights
    n = maximum - minimum

    edge_alpha = map(lambda x:round(x,4), np.linspace(0.3,0.9,n))

    for t,a in zip(range(minimum,maximum+1),edge_alpha):
        nx.draw_networkx_edges(G,pos=pos,edgelist=extractor(G,t),alpha=a,width=5*a)

    nx.draw_networkx_nodes(G,pos=pos,nodelist=G.nodes(),node_size=35)

    plt.axis('off')
    plt.show()



def main():

    path_edges = os.getcwd() + "/user_edge_9.txt"

    G = nx.Graph()
    G.add_weighted_edges_from(data_import(path_edges))

    graph_draw(G)

if __name__ == "__main__":
    main()
