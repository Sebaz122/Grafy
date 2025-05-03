import zad1 as z1
import zad2 as z2
import zad3 as z3
import networkx as nx
import functions as f
import pprint



if __name__=="__main__":
    # G=nx.Graph()
    # adj_matrix=[[0,0,1,0,1,1],[0,0,0,0,1,1],[1,0,0,1,1,0],[0,0,1,0,0,0],[1,1,1,0,0,1],[1,1,0,0,1,0]] 
    # incydency_matrix=[[1,1,1,0,0,0,0,0],[0,0,0,1,1,0,0,0],[1,0,0,0,0,1,1,0],[0,0,0,0,0,1,0,0],[0,1,0,1,0,0,1,1],[0,0,1,0,1,0,0,1]] 
    # adj_list=[[2,4,5],[4,5],[0,3,4],[2],[0,1,2,5],[0,1,4]]

    
    # G=z1.graph_from_adj_matrix(G,adj_matrix)
    # z2.draw_graph_circular(G, "imgs/zad1/zad1")
    # G=graph_from_incidency_matrix(G,incydency_matrix)
    # draw_graph_circular(G)
    # G=graph_from_adj_list(G,adj_list)
    # draw_graph_circular(G)

    # adj_matrix_to_inc_matrix(adj_matrix)
    # adj_matrix_to_adj_list(adj_matrix)
    # adj_list_to_adj_matrix(adj_list)
    # adj_list_to_inc_matrix(adj_list)
    # inc_matrix_to_adj_list(incydency_matrix)
    # z1.inc_matrix_to_adj_matrix(incydency_matrix)

    input_matrix = [
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
]
    G=nx.Graph()
    G=z1.graph_from_adj_matrix(G,input_matrix)
    z2.draw_graph_circular(G,"imgs/zad1/graph_from_adj_matrix")

    adj_list=z1.adj_matrix_to_adj_list(input_matrix)
    G=z1.graph_from_adj_list(G,adj_list)
    z2.draw_graph_circular(G,"imgs/zad1/graph_from_adj_list")
    pprint.pprint(adj_list)

    inc_matrix=z1.adj_matrix_to_inc_matrix(input_matrix)
    G=z1.graph_from_incidency_matrix(G,inc_matrix)
    z2.draw_graph_circular(G,"imgs/zad1/graph_from_inc_matrix")
    pprint.pprint(inc_matrix)

    G=z3.generating_graph_random_1(7,10)
    z2.draw_graph_circular(G,"imgs/zad3/graph_generated_1")

    G=z3.generating_graph_random_2(7,0.5)
    z2.draw_graph_circular(G, "imgs/zad3/graph_generated_2")


    