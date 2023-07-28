import matplotlib.pyplot as plt
import networkx as nx
import random


def tworz_lab(szer, wys):
    labi = nx.grid_2d_graph(szer - 1, wys - 1)

    for kraw in labi.edges():
        labi[kraw[0]][kraw[1]]['weight'] = random.randrange(3, 20)

    MSt = nx.minimum_spanning_tree(labi, weight='weight')



    finalny = nx.grid_2d_graph(szer, wys)
    for kraw in finalny.edges():
        if ((kraw[0][0], kraw[0][1] - 1), (kraw[1][0] - 1, kraw[1][1])) in MSt.edges():
            finalny.remove_edge(*kraw)
        if ((kraw[0][0] - 1, kraw[0][1]), (kraw[1][0], kraw[1][1] - 1)) in MSt.edges():
            finalny.remove_edge(*kraw)

    return finalny



def perfektuje(szer, wys):
    labi = nx.grid_2d_graph(szer, wys)
    fin_labi = nx.grid_2d_graph(szer + 1, wys + 1)

    for i, j in labi.edges():
        labi[i][j]['weight'] = random.randrange(4, 20)

    MSt = nx.minimum_spanning_tree(labi)


    for kraw in fin_labi.edges():
        if ((kraw[0][0], kraw[0][1] - 1), (kraw[1][0] - 1, kraw[1][1])) in MSt.edges():
            fin_labi.remove_edge(*kraw)
        if ((kraw[0][0] - 1, kraw[0][1]), (kraw[1][0], kraw[1][1] - 1)) in MSt.edges():
            fin_labi.remove_edge(*kraw)

    return fin_labi, MSt


def generate_special_maze(szer, wys):
    labi = nx.grid_2d_graph(szer + 1, wys + 1)

    for i in range(1, wys + 1):

        labi.remove_edge((0, i), (0, i - 1))
        labi.remove_edge((szer, i), (szer, i - 1))

    return labi


def zadanie_1():
    print("zadanie 1 :")
    width=int(input("podaj szerokosc:"))
    height=int(input("podaj wysokosc: "))
    labyrinth, nwmm = perfektuje(width, height)

    plt.figure(figsize=(width, height))
    ax = plt.gca()
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    for point in labyrinth.edges():
        ax.plot([point[0][0], point[1][0]], [point[0][1], point[1][1]], 'b')

    plt.show()


def zadanie_2():
    print('Zadanie 2')
    width = int(input("podaj szerokosc:"))
    height = int(input("podaj wysokosc: "))
    labyrinth, minimum_spanning_tree = perfektuje(width, height)

    plt.figure(figsize=(width, height))
    ax = plt.gca()
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    for point in labyrinth.edges():
        ax.plot([point[0][0], point[1][0]], [point[0][1], point[1][1]], 'b')


    s_x= int(input("podaj x startowy:"))
    s_y= int(input("podaj y startowy: "))

    pocz = (s_x, s_y)

    e_x = int(input("podaj x startowy:"))
    e_y = int(input("podaj y startowy: "))

    kon = (e_x, e_y)

    droga = nx.shortest_path(minimum_spanning_tree, pocz, kon)

    for i in range(len(droga) - 1):
        p1 = droga[i]
        p2 = droga[i + 1]
        ax.plot([p1[0] + 0.648, p2[0] + 0.648], [p1[1] + 0.648, p2[1] + 0.648], 'r', linewidth=5)

    ax.text(pocz[0], pocz[1], '*', color='gold', fontsize=50)

    ax.text(kon[0], kon[1], '*', color='gold', fontsize=50,)
    plt.show()


def zadanie_3():
    print('Zadanie 3')

    width = int(input("podaj szerokosc:"))
    height = int(input("podaj wysokosc: "))

    labyrinth, minimum_spanning_tree = perfektuje(width, height)

    plt.figure(figsize=(width, height))
    ax = plt.gca()
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    for point in labyrinth.edges():
        ax.plot([point[0][0], point[1][0]], [point[0][1], point[1][1]], 'b')

    s_x = int(input("podaj x startowy:"))
    s_y = int(input("podaj y startowy: "))

    pocz = (s_x, s_y)

    e_x = int(input("podaj x startowy:"))
    e_y = int(input("podaj y startowy: "))

    kon = (e_x, e_y)

    path = nx.shortest_path(minimum_spanning_tree, pocz, kon)

    for u, v in minimum_spanning_tree.edges():
        if (u != pocz and u != kon) or (v != pocz and v != kon):
            ax.plot([u[0] + 0.6, v[0] + 0.6], [u[1] + 0.6, v[1] + 0.6], 'yellow', linewidth=3)

    for i in range(len(path) - 1):
        p1 = path[i]
        p2 = path[i + 1]
        ax.plot([p1[0] + 0.6, p2[0] + 0.6], [p1[1] + 0.6, p2[1] + 0.6], 'r', linewidth=3)

    ax.text(pocz[0], pocz[1], '*', color='gold', fontsize=50)

    ax.text(kon[0], kon[1], '*', color='gold', fontsize=50, )
    plt.show()

zadanie_1()
zadanie_2()
zadanie_3()
