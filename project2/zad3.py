from graph_utils import *

def components(graph):
    visited = {v: -1 for v in graph}
    component_id = 0
    component_map = []

    for vertex in graph:
        if visited[vertex] == -1:
            component_id += 1
            dfs_component_mark(graph, vertex, component_id, visited)

    for v in visited:
        component_map.append((visited[v], v))

    counts = [cid for cid, _ in component_map]
    largest_id = max(set(counts), key=counts.count)
    largest_component = [v for cid, v in component_map if cid == largest_id]

    return component_map, largest_component

def dfs_component_mark(graph, current, component_id, visited):
    visited[current] = component_id
    for neighbor in graph[current]:
        if visited[neighbor] == -1:
            dfs_component_mark(graph, neighbor, component_id, visited)


def task3():
    graph = {f"v{i}": set() for i in range(1, 6)}
    edges = [
        ("v1", "v2"),
        ("v3", "v4"), ("v4", "v5"), ("v5", "v3")
    ]
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    draw_graph(graph, filename="zad3.png")

    comp_map, largest = components(graph)
    print("All components:", comp_map)
    print("Largest component:", largest)

if __name__ == "__main__":
    task3()
