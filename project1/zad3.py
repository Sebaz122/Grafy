import networkx as nx
import matplotlib.pyplot as plt
import random

def generating_graph_random_1(n,k):
    """
    Funkcja przyjmuje ilość wierzchołków grafu oraz krawędzi a następnie generuje graf losowy tworząc wszystkie możliwe krawędzie, a następnie wybierając z nich losowe k-krawędzi używając 
    funkcji random sample.

    Params in : n - liczba wierzchołków grafu, k - liczba krawędzi grafu
    Params out : G - losowo wygenerowany graf
    """
    if k<0 or k>(n*(n-1)//2): # sprawdzenie, czy liczba krawędzi jest prawidłowo podana
        raise ValueError("Niepoprawna wartośc k")
    
    G=nx.Graph()
    for i in range(n):
        G.add_node(i)
    
    edges=[(i,j) for i in range(n) for j in range (i+1,n)]
    
    graph_edges=random.sample(edges,k)

    for i in range(k):
        G.add_edge(graph_edges[i][0],graph_edges[i][1])

    return G


def generating_graph_random_2(n,p):
    """
    Funkcja przyjmuje ilość wierzchołków grafu prawdopodobieństwo wystąpienia krawędzi pomiędzy dwoma wierzchołkami i losowo generuje graf. 

    Params in : n - liczba wierzchołków grafu, p - prawdopodobieństwo wystąpienia krawędzi pomiędzy dwoma wierzchołkami
    Params out : G - losowo wygenerowany graf
    """

    if p>1 or p<0:
        raise ValueError("P musi byc w zakresie [0,1]")
    
    G=nx.Graph()
    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(i+1,n):
            if random.random()<p:
                G.add_edge(i,j)
    return G