import random
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

def canGraphBeCreated(sequence):
    seq = sequence[:]
    if sum(seq) % 2 == 1:
        return False
    while True:
        seq = sorted(seq, reverse=True)
        if seq[0] == 0:
            return True
        v = seq[0]
        seq = seq[1:]
        if v > len(seq):
            return False
        for i in range(v):
            seq[i] -= 1
            if seq[i] < 0:
                return False

def createGraphFromSequence(sequence):
    if not canGraphBeCreated(sequence):
        return None
    n = len(sequence)
    graph = {i: set() for i in range(n)}
    nodes = [(i, deg) for i, deg in enumerate(sequence)]
    while True:
        nodes.sort(key=lambda x: x[1], reverse=True)
        if nodes[0][1] == 0:
            break
        v, deg = nodes[0]
        nodes = nodes[1:]
        if deg > len(nodes):
            return None
        for i in range(deg):
            u, d = nodes[i]
            graph[v].add(u)
            graph[u].add(v)
            nodes[i] = (u, d - 1)
    return graph

def canEdgesBeSwapped(graph, edge1, edge2):
    a, b = edge1
    c, d = edge2
    if len({a, b, c, d}) < 4:
        return False
    if d in graph[a] or c in graph[b]:
        return False
    return True

def randomizeNotDirectedGraphWithoutChangingDegrees(graph, count=10):
    newGraph = deepcopy(graph)
    edges = list({(min(u, v), max(u, v)) for u in newGraph for v in newGraph[u] if u < v})
    loopCount = 0
    for _ in range(count):
        while True:
            if loopCount > 1000:
                return newGraph
            e1 = random.choice(edges)
            e2 = random.choice(edges)
            if e1 == e2:
                continue
            if canEdgesBeSwapped(newGraph, e1, e2):
                a, b = e1
                c, d = e2
                for x, y in [(a, b), (c, d)]:
                    newGraph[x].remove(y)
                    newGraph[y].remove(x)
                for x, y in [(a, d), (b, c)]:
                    newGraph[x].add(y)
                    newGraph[y].add(x)
                edges.remove(e1)
                edges.remove(e2)
                edges.append((min(a, d), max(a, d)))
                edges.append((min(b, c), max(b, c)))
                break
            loopCount += 1
    return newGraph

def printGraph(graph):
    for v in sorted(graph):
        print(f"{v}: {sorted(graph[v])}")

def draw_graph(graph, filename=None):
    G = nx.Graph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    if filename:
        plt.savefig(filename)
    plt.show()
