import networkx as nx
import matplotlib.pyplot as plt
import random
import functions as f


def graph_from_adj_matrix(G:nx.Graph ,matrix):
    """
    Funkcja przyjmuje graf oraz macierz sąsiedztwa. Jeżeli graf nie jest pusty to go czyści, sprawdza czy macierz sąsiedztwa jest w poprawnym formacie,
    a następnie iteruje po wierszach do przekątnej macierzy, aby nie powtarzać wartości, bo macierz jest symetryczna, i dodaje wierzchołki oraz krawędzie do grafu.

    Params in : G - graf z biblioteki networkx, matrix - macierz sąsiedztwa
    Params out : G - uzupełniony graf na podstawie macierzy sąsiedztwa
    """

    rows=len(matrix)
    cols=len(matrix)
    if G.nodes != 0 or G.edges != 0: # sprawdzenie czy graf jest pusty
        G.clear()

    f.is_adj_matrix(matrix) # sprawdzenie czy macierz jest w poprawnym formacie
            
    
    for i in range(rows):
        G.add_node(i)
        for j in range(i+1):
            if matrix[i][j] == 1:
                G.add_edge(i,j)

    return G

def graph_from_incidency_matrix(G:nx.Graph, matrix):
    """
    Funkcja przyjmuje graf oraz macierz incydencji. Jeżeli graf nie jest pusty to go czyści, sprawdza, czy macierz incydencji jest w poprawnym formacie,
    a następnie iteruje po kolumnach macierzy i jej elementach, dodaje indeksy jedynek do listy edge_indexes, dodaje krawędź do grafu oraz czyści listę edge_indexes. 

    Params in : G - graf z biblioteki networkx, matrix - macierz incydencji
    Params out : G - uzupełniony graf na podstawie macierzy incydencji
    """

    num_of_cols=len(matrix[0])
    num_of_rows=len(matrix)
    edge_indexes=[]

    if G.nodes != 0 or G.edges != 0: # sprawdzenie czy graf jest pusty
        G.clear()

    f.is_inc_matrix(matrix)

    edge_indexes.clear()

    for j in range(num_of_cols): 
        for i in range(num_of_rows):
            G.add_node(i)
            if matrix[i][j]==1:
                edge_indexes.append(i)
        G.add_edge(edge_indexes[0],edge_indexes[1])
        edge_indexes.clear()

    return G


def graph_from_adj_list(G:nx.Graph ,adj_list):
    """
    Funkcja przyjmuje graf oraz listę sąsiedztwa. Jeżeli graf nie jest pusty to go czyści, sprawdza, czy lista sąsiedztwa jest w poprawnym formacie,
    a następnie iteruje po wierszach listy i jej elementach oraz dodaje krawędzie do grafu.

    Params in : G - graf z biblioteki networkx, adj_list - lista sąsiedztwa
    Params out : G - uzupełniony graf na podstawie listy sąsiedztwa
    """
    num_of_rows=len(adj_list)

    if G.nodes != 0 or G.edges != 0: # sprawdzenie czy graf jest pusty
        G.clear()
    
    f.is_adj_list(adj_list) # sprawdzenie czy macierz jest w poprawnym formacie
    
    for i in range(num_of_rows):
        G.add_node(i)
        for j in adj_list[i]:
            G.add_edge(i,j)

    return G

def adj_matrix_to_inc_matrix(matrix:list):
    """
    Funkcja przyjmuje macierz sąsiedztwa. Sprawdza czy jest w poprawnym formacie, a następnie iteruje po wierszach listy i jej elementach do przekątnej, dodając 
    indeksy wiersza i elementu, w którym występuje jedynka do listy krawędzi. Tworzy macierz incydencji, wypełnia ją zerami w wymiarze rows x edges_count (wierzchołki x ilość krawędzi), po czym
    kolejna pętla iteruje po edges_count i ustawia odpowiednie wartości na 1.

    Params in : matrix - macierz sąsiedztwa
    Params out : inc_matrix - macierz incydencji
    """
    
    rows=len(matrix)
    edges_list=[]
    f.is_adj_matrix(matrix) # sprawdzenie, czy macierz jest macierzą sąsiedztwa
    
    for i in range(rows):
        for j in range(i+1):
            if matrix[i][j] == 1:
                edges_list.append([i,j])

    edges_count=len(edges_list)
    inc_matrix=[[] for _ in range(rows)]

    for i in range(rows):
        inc_matrix[i]=[0 for _ in range(edges_count)]

    for i in range(edges_count):
        edge=edges_list[i]
        inc_matrix[edge[0]][i]=1
        inc_matrix[edge[1]][i]=1
             
    return inc_matrix

def adj_matrix_to_adj_list(matrix):
    """
    Funkcja przyjmuje macierz sąsiedztwa. Sprawdza czy jest w poprawnym formacie, a następnie iteruje po wierszach i elementach wiersza, sprawdzając, czy wartośc jest jedynką.
    Jeżeli jest, to dodaje do odpowiedniego wiersza listy sąsiedztwa indeks elementu.

    Params in : matrix - macierz sąsiedztwa
    Params out : adj_list - lista sąsiedztwa
    """
    rows=len(matrix)
    cols=rows
    adj_list=[[] for i in range(rows)]

    f.is_adj_matrix(matrix) # sprawdzenie, czy macierz jest macierzą sąsiedztwa

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==1:
                adj_list[i].append(j+1) # +1 bo w inpucie tak było
    
    return adj_list



def adj_list_to_adj_matrix(adj_list):
    """
    Funkcja przyjmuje listę sąsiedztwa. Sprawdza czy jest w poprawnym formacie, wypełnia macierz sąsiedztwa zerami, a następnie iterując po wierszach i ich elementach wypełnia macierz sąsiedztwa
    w odpowiednich miejsach zerami

    Params in : adj_list - lista sąsiedztwa
    Params out : adj_matrix - macierz sąsiedztwa
    """
    rows=len(adj_list)
    cols=rows
    adj_matrix=[[] for i in range(rows)]

    f.is_adj_list(adj_list) # sprawdzenie czy lista jest w poprawnym formacie

    for i in range(rows):
        for j in range(cols):
            adj_matrix[i].append(0)

    for i in range(rows):
        for j in adj_list[i]:
            adj_matrix[i][j]=1

    return adj_matrix



def adj_list_to_inc_matrix(adj_list):
    """
    Funkcja przyjmuje listę sąsiedztwa. Następnie, używając poprzednio napisanych funkcji konwertuje ją na macierz incydencji.

    Params in : adj_list - lista sąsiedztwa
    Params out : inc_matrix - macierz incydencji
    """

    adj_matrix=adj_list_to_adj_matrix(adj_list)
    inc_matrix=adj_matrix_to_inc_matrix(adj_matrix)

    return inc_matrix


def inc_matrix_to_adj_list(matrix):
    """
    Funkcja przyjmuje macierz incydencji. Sprawdza, czy jest w poprawnym formacie. Następnie iteruje po kolumnach i jej elementach, jak napotka jedynkę to dodaje do listy krawędzi
    odpowiedni indeks. Jeżeli lista krawędzi ma dwa indeksy, dodaje tą krawędź do listy sąsiedztwa na odpowiednich miejscach i czyści listę krawędzi.

    Params in : matrix - macierz incydencji
    Params out : adj_list - lista sąsiedztwa
    """
    num_of_cols=len(matrix[0])
    num_of_rows=len(matrix)
    adj_list=[[] for i in range(num_of_rows)]
    edges=[]

    f.is_inc_matrix(matrix) # sprawdza czy macierz jest w poprawnym formacie

    for j in range(num_of_cols):
        for i in range(num_of_rows):
            if matrix[i][j]==1:
                edges.append(i)
                if len(edges)==2:
                    adj_list[edges[0]].append(edges[1])
                    adj_list[edges[1]].append(edges[0])
                    edges.clear()
    
    return adj_list


def inc_matrix_to_adj_matrix(matrix): 
    """
    Funkcja przyjmuje macierz incydencji. Sprawdza, czy jest w poprawnym formacie. Tworzy macierz sąsiedztwa i wypełnia wiersze zerami. Następnie iteruje po kolumnach macierzy incydencji
    i ich elementach, sprawdzając, czy są jedynką. Jeśli tak, i lista przetrzymująca indeksy jest pusta, to dodaje do niej indeks jedynki. Jeśli element jest jedynką, a 
    lista przetrzymująca indeks nie jest pusta, to dodaje do niej indeks jedynki, na tych indeksach macierzy sąsiedztwa ustawia jeden oraz czyści liste indeksów.

    Params in : matrix - macierz incydencji
    Params out : adj_matrix - macierz sąsiedztwa
    """
    index_hold=[]
    rows=len(matrix)
    cols=rows
    inc_matrix_cols=len(matrix[0])
    adj_matrix=[[]for i in range(rows)]

    f.is_inc_matrix(matrix) # sprawdza czy macierz jest w poprawnym formacie

    for i in range(cols):
        for j in range(rows):
            adj_matrix[i].append(0)

    for j in range(inc_matrix_cols):
        for i in range(rows):
            if(matrix[i][j])==1 and len(index_hold)==0:
                index_hold.append(i)
            elif(matrix[i][j]==1) and len(index_hold)!=0:
                index_hold.append(i)
                adj_matrix[index_hold[0]][index_hold[1]]=1
                adj_matrix[index_hold[1]][index_hold[0]]=1
                index_hold.clear()
                
    return adj_matrix

