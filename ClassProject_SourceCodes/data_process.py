import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import numpy as np
import os


def data_import(file_name):
    # input -> the name of the data file
    # output -> an edge list, user list and track list

    edge_list = []
    users = []
    tracks = []

    with open(file_name,"r") as f:
        for e in f.readlines():
            e = e.replace(" ",",").replace("\n","") # 1 23\n -> 1,23
            e = e.split(",") # "1,23" -> ["1","23"]
            edge_list.append((int(e[0]),str(e[1])))
            users.append(int(e[0]))
            tracks.append(str(e[1]))

    return edge_list,users,tracks


def weight_dist(B):

    ws = [] # a list of weghits
    edge_list = B.edges()
    bins = [e for e in range(1,50)]

    for i,j in edge_list:
        ws.append(B[i][j]["weight"])
        #if B[i][j]["weight"] == 16:
        #    print(i,j)

    return np.histogram(ws,bins=bins)

def threshold(G,t):
    # input -> a graph G and a float value t, threshold.
    # output -> a graph

    edges = G.edges()

    for i,j in edges:

        if G[i][j]["weight"] >= t:
            continue

        else:
            G.remove_edge(i,j)

    return G

def Bipartite(users,tracks,edge_list):

    B = nx.Graph() # Bipartite Graph
    B.add_nodes_from(users,bipartite=0)
    B.add_nodes_from(tracks,bipartite=1)
    B.add_edges_from(edge_list)

    return B

def graph_draw(G):
    labels = {}

    for e in G.nodes():
        labels[e] = e

    pos = nx.spring_layout(G)

    nx.draw_networkx_labels(G,pos=pos,labels=labels,font_size=15)
    nx.draw(G,pos=pos,node_size=50)
    plt.show()


def main():
    path = os.getcwd() + "/Sampled_Data/second_guys/"

    edge_list,users,tracks = data_import(path+"merged2.txt")

    B = Bipartite(users,tracks,edge_list)

    projected_B = bipartite.weighted_projected_graph(B,users)
    print(weight_dist(projected_B))
    #print("number of tracks",len(projected_B.nodes()))
    #B_threshold = threshold(projected_B,6)
    #giant = max(nx.connected_component_subgraphs(B_threshold), key=len)

    #components = []

    with open("edge_list2_users.txt","w") as f:
        for i,j in projected_B.edges_iter():
            f.write(str(i)+ " " + str(j) +" "+ str(projected_B[i][j]["weight"]) +"\n")

    #for g in nx.connected_component_subgraphs(B_threshold):
    #    if len(g.nodes()) < 3:
    #        continue
    #    components.append(g)

    #graph_draw(nx.union_all(components))


if __name__ == "__main__":
    main()