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
            e = e.replace(" ",",").replace("\n","") # 1 23\n -> 1,23
            i,j,w = e.split(",") # "1,23" -> ["1","23"]
            edge_list.append((str(i),str(j),int(w)))


    return edge_list

def target_open(file_name):

    result = []

    with open(file_name,"r") as f:
        for e in f.readlines():
            result.append(e.replace("\n",""))

    return result

def group_import(filename):

    groups = []

    with open(filename) as f:
        for e in f.readlines():
            e = e.replace("\n","")
            e = e.split(" ") # should be like ["ABK","HKJS",...]
            groups.append(e)

    return groups


def extractor(G,t):
    # input -> a graph G and an int t
    # output -> a list of edges whose weight is t
    return [(i,j) for i,j,attr in G.edges_iter(data=True) if attr["weight"] == t]

def min_or_max(G,func=max):
    return func([attr["weight"] for i,j,attr in G.edges_iter(data=True)])


def targeted_draw(G,target,group):

    pos = nx.spring_layout(G)

    minimum = min_or_max(G,min) # the minimum of weights
    maximum = min_or_max(G,max)# the maximum of weights
    n = maximum - minimum

    edge_alpha = map(lambda x:round(x,4), np.linspace(0.25, 0.8,n))

    for t,a in zip(range(minimum,maximum+1),edge_alpha):
        nx.draw_networkx_edges(G,pos=pos,edgelist=extractor(G,t),alpha=a,width=5*a)

    others = set(G.nodes())
    others.difference_update(target)

    nx.draw_networkx_nodes(G,pos=pos,nodelist=others,node_size=50,node_color="b")
    #nx.draw_networkx_nodes(G,pos=pos,nodelist=group,node_size=50,node_color="g")
    nx.draw_networkx_nodes(G,pos=pos,nodelist=target,node_size=50,node_color="r")

    plt.axis('off')
    plt.show()


def graph_draw(G,groups):

    labels = {}
    for e in G.nodes():
        labels[e] = e

    pos = nx.spring_layout(G)
    node_color = ["#FFFF00","#FF0000","#00FF00","#9900FF","#0000FF","#008080",
                  "#00FFFF","#000080","#FF00FF"]

    minimum = min_or_max(G,min) # the minimum of weights
    maximum = min_or_max(G,max)# the maximum of weights
    n = maximum - minimum

    #nx.draw_networkx_labels(G,pos=pos,labels=labels,font_size=15)
    edge_alpha = map(lambda x:round(x,4), np.linspace(0.25, 0.8,n))

    for t,a in zip(range(minimum,maximum+1),edge_alpha):
        nx.draw_networkx_edges(G,pos=pos,edgelist=extractor(G,t),alpha=a,width=5*a)

    for g,color in zip(groups,node_color):
        nx.draw_networkx_nodes(G,pos=pos,nodelist=g,node_size=50,node_color=color)

    plt.axis('off')
    plt.show()

def main():
    path_edge = os.getcwd() + "/Processed_Data/"
    path_partition = os.getcwd() + "/music_partition/"
    edges = data_import(path_edge+"edge_list2_t_12.txt")
    groups = group_import(path_partition+"graph_partition.txt")
    target = target_open("target_50_play.txt")

    G =nx.Graph()
    G.add_weighted_edges_from(edges)

    components = []
    for g in nx.connected_component_subgraphs(G):
        if len(g.nodes()) < 3:
            continue
        components.append(g)

    #graph_draw(nx.union_all(components),groups)
    targeted_draw(nx.union_all(components),target,groups[1])

if __name__ == "__main__":
    main()