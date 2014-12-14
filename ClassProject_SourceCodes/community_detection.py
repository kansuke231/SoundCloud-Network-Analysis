

import networkx as nx
import itertools
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


def all_weights(G):
    edges = G.edges()
    w = 0  # weights of all edges
    for i,j in edges:
        w+=G[i][j]["weight"]

    return w


def e_rs(G,g1,g2):

    sigma = 0
    for i,j in G.edges():
        if ((i in g1) and (j in g2)) or \
           ((i in g2) and (j in g1)):
            sigma+=G[i][j]["weight"]

    return sigma/float(2*all_weights(G))


def a_r(G,group):
    sigma = sum([G.degree(x,weight="weight") for x in G.nodes() if x in group])
    return sigma/float(2*all_weights(G))


def e_rr(G,g):
    sigma =  sum([G[i][j]["weight"] for i,j in G.edges() if (i in g) and (j in g)])
    return sigma/float(all_weights(G))

def Q(G,groups):
    return sum([e_rr(G,groups[g])-(a_r(G,groups[g]))**2
                for g in groups.keys()])


def delta_Q(G,g1,g2):
    # input -> a Graph G and two groups, g1 and g2
    # output -> delta Q
    return 2*(e_rs(G,g1,g2)-(a_r(G,g1)*a_r(G,g2)))

def greedy_agglo(G,groups):

    delta_max = -1
    merge = () # two groups to be merged

    for e in itertools.combinations(groups.keys(),2):
        result = delta_Q(G,groups[e[0]],groups[e[1]])
        if result > delta_max:
            delta_max = result
            merge = e

    # merging the two groups
    groups[merge[0]]+=groups[merge[1]]
    groups.pop(merge[1],None)

    q = round(Q(G,groups),6)

    #print("Q",q,"Delta Q",round(delta_max,6),merge)
    return groups,q

def main():
    path = os.getcwd() + "/Processed_Data/"
    edges = data_import(path+"edge_list2_t_11.txt")

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    groups =  {x:[x] for x in G.nodes()}

    Qs = [] # the sequence of Q over merging
    q = Q(G,groups)

    Qs.append(q)

    while True:
        prev_q = q
        prev_G = groups
        groups,q = greedy_agglo(G,groups=groups)

        if q < prev_q:
            groups = prev_G
            break

        Qs.append(q)
        print(groups,q)

    with open("graph_partition.txt","w") as f:
        for e in groups.keys():
            row = ""
            for i in groups[e]:
                row = row + " " + i
            f.write(row + "\n")

    for e in groups.keys():
        print(groups[e])

    for e in Qs:
        print(e)


if __name__ == "__main__":
    main()

