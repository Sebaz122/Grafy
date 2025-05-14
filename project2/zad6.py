from graph_utils import * 

def prepareGraphForHamilton(adj_list):
    return {k: set(v) for k, v in adj_list.items()}

def hamiltonCycle(graph):
    n = len(graph)
    vertices = list(graph)

    def dfs(path):
        if len(path) == n:
            if path[0] in graph[path[-1]]:
                return path + [path[0]]
            return None
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                result = dfs(path + [neighbor])
                if result:
                    return result
        return None

    for start in vertices:
        result = dfs([start])
        if result:
            return result
    return None

def buildGraph(edges):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)
    return graph

if __name__ == "__main__":
    edges1 = [
        ("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("5", "1"),
        ("1", "3"), ("2", "4"), ("3", "5")
    ]
    g1 = buildGraph(edges1)
    result1 = hamiltonCycle(g1)
    print("Hamilton cycle 1:", result1)
    draw_graph(g1, "zad6_Hamilton1.png")

    edges2 = [
        ("1", "2"), ("2", "3"), ("2", "4"), ("2", "5")
    ]
    g2 = buildGraph(edges2)
    result2 = hamiltonCycle(g2)
    print("Hamilton cycle 2:", result2)
    draw_graph(g2, "zad6_Hamilton2.png")
