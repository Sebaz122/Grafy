import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_circular(G:nx.Graph, path):
    """
    Funkcja przyjmuje graf do narysowania oraz ścieżkę, do której zapisuje się narysowany graf. Za pomocą funkcji draw z biblioteki networkx rysuje graf równomiernie rozłożony na okręgu.

    Params in : G - poprawny graf do narysowania
    Params out : brak
    """
    pos=nx.circular_layout(G)
    nx.draw(G,pos,with_labels=True)
    circle = plt.Circle((0, 0), 1.05, color='red', fill=False, linestyle=':', linewidth=2)
    plt.gca().add_patch(circle)
    plt.savefig(path)
    plt.clf()