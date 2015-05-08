import matplotlib.pyplot as plt

def plotter(Qs):
    x_axis = [x for x in range(len(Qs))]
    plt.plot(x_axis,Qs,"o")
    plt.xlim(-1,210)
    plt.ylim(-0.1,0.5)
    plt.xlabel("number of merging")
    plt.ylabel("Q")
    plt.show()

def data_import(filename):

    Qs = []
    # USE THE TIME MACHINE FOR FIXING THE DATA!!!!
    with open(filename,"r") as f:
        for e in f.readlines():
            e = e.replace("\n","")
            Qs.append(float(e))

    return Qs

def main():
    plotter(data_import("graph_partition_Q.txt"))


if __name__ == "__main__":
    main()
