from graph_utils import *

def createK_RegularGraph(k, size):
    sequence = [k] * size
    if not canGraphBeCreated(sequence):
        return None
    graph = createGraphFromSequence(sequence)
    return randomizeGraphWithoutChangingDegrees(graph)

if __name__ == "__main__":
    graph = createK_RegularGraph(3, 8)
    print("Graph:")
    printGraph(graph)
    draw_graph(graph, 'zad5.png')
