import random
from copy import deepcopy

from graph_utils import *

def is_eulerian(graph):
    return all(len(neighbors) % 2 == 0 for neighbors in graph.values())

# Zwraca wszystkie spójne składowe grafu
def connected_components(graph):
    visited = set()
    components = []

    def dfs(v, component):
        visited.add(v)
        component.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(comp)
    return components

def count_connected_components(graph):
    return len(connected_components(graph))

# Sprawdza, czy dana krawędź jest mostem, tzn. czy po jej usunięciu rośnie liczba składowych
def is_bridge(graph, edge):
    u, v = edge

    graph[u].remove(v)
    graph[v].remove(u)
    count_before = count_connected_components(graph)

    graph[u].add(v)
    graph[v].add(u)
    count_after = count_connected_components(graph)
    return count_after > count_before

# Szuka cyklu Eulera w grafie (algorytm Fleury’ego)
def find_euler_cycle(graph):
    if not is_eulerian(graph):
        return None
    graph = deepcopy(graph)
    start = next(iter(graph))
    cycle = []

    def traverse(v):
        for u in list(graph[v]):
            # unikamy wielokrotnych przejść przez krawędź
            if (u, v) not in cycle and (v, u) not in cycle:
                if len(graph[v]) == 1 or not is_bridge(graph, (v, u)):
                    graph[v].remove(u)
                    graph[u].remove(v)
                    traverse(u)
                    cycle.append((v, u))

    traverse(start)
    return cycle[::-1]

# Generuje losowy nieskierowany graf
def generate_random_graph(n, p):
    graph = {f'v{i}': set() for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                u, v = f'v{i}', f'v{j}'
                graph[u].add(v)
                graph[v].add(u)
    return graph

# Zwraca listę wierzchołków o nieparzystym stopniu
def get_odd_degree_nodes(graph):
    return [v for v in graph if len(graph[v]) % 2 == 1]

# Generuje losowy graf eulerowski (spójny oraz wszystkie wierzch parzystego stopnia)
def generate_random_euler_graph(n=8, p=0.3):
    while True:
        graph = generate_random_graph(n, p)
        comps = connected_components(graph)

        if len(comps) > 1:
            for a, b in zip(comps[:-1], comps[1:]):
                u = random.choice(a)
                v = random.choice(b)
                graph[u].add(v)
                graph[v].add(u)

        odd_nodes = get_odd_degree_nodes(graph)
        if len(odd_nodes) % 2 == 0:
            break 

    for i in range(0, len(odd_nodes), 2):
        u, v = odd_nodes[i], odd_nodes[i + 1]
        if u != v and v not in graph[u]:
            graph[u].add(v)
            graph[v].add(u)
        else:
            return generate_random_euler_graph(n, p)

    if is_eulerian(graph) and count_connected_components(graph) == 1:
        return graph
    else:
        return generate_random_euler_graph(n, p)


if __name__ == "__main__":
    g = generate_random_euler_graph(8)
    cycle = find_euler_cycle(g)
    print("Euler cycle:")
    print(cycle)
    draw_graph(g, 'zad4.png')
