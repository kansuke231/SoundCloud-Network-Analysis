

node_color = ["#FFFF00","#FF0000","#00FF00","#008000",
              "#0000FF","#008080","#00FFFF","#000080","#FF00FF"]

def decoder(string):

    result = 0
    digit_decoder = lambda x: ord(x)-ord("A")

    for i,e in enumerate(reversed(string)):
        result+=digit_decoder(e)*26**i

    return result

def data_import(filename):

    i = 0 # group index
    partition = {}

    with open(filename,"r") as f:
        for e in f.readlines():
            e = e.replace(" ",",").replace("\n","") # KCOUQU LQVXKL
            e = e.split(",") # KCOUQU,LQVXKL -> [KCOUQU,LQVXKL]
            partition[i] = e
            i+=1

    return partition



def data_count_import(filename):

    result = []

    with open(filename,"r") as f:
        for e in f.readlines():
            e = e.replace(" ",",").replace("\n","")
            e = e.split(",")
            result += [(int(e[0]),str(e[1]),int(e[2]),int(e[3]))]

    return result