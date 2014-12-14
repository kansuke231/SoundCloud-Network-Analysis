import os
import operator
from itertools import izip
from collections import Counter

def data_import(path):

    rows = []

    with open(path,"r") as f:
        for e in f.readlines():
            rows.append(e)

    return rows

def pairwise(iterable):
    # python recipe found at
    # http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a = iter(iterable)
    return izip(a, a)

def clean_up(string):
    # makes a weird string clean
    indices = [i for i,x in enumerate(string) if x == '"']
    assert len(indices)%2 == 0

    for i,j in pairwise(indices):
        replaced = string[i:j+1].replace(" ","-").replace('"'," ")
        string = string[:i] + replaced + string[j+1:]

    return string[:-1]

def tag_genre_counter(index):

    path = os.getcwd() + "/tags_genre/"+"group_%s_tag.txt" %str(index)
    rows = data_import(path)

    words = []

    for e in rows:
        string = clean_up(e).lower()
        words+=[e for e in string.split(" ") if e != ""]

    count = Counter(words)
    sorted_c = sorted(count.items(), key=operator.itemgetter(1),reverse=True)

    with open("tag_genre_freq_tab%s.txt"%str(index),"w") as f:
        for name,n in sorted_c:
            f.write(str(name)+"\t"+str(n)+"\n")

    for e in sorted_c:
        print(e)


def main():
    for e in range(9):
        tag_genre_counter(e)

if __name__ == "__main__":
    main()