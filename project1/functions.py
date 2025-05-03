
def is_adj_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix)

    if rows != cols: # sprawdzenie czy macierz jest w poprawnym formacie
        raise ValueError("Macierz ma niepoprawne wymiary")

    for i in range(rows): # sprawdzenie czy macierz jest w poprawnym formacie
        for j in range(cols):
            if matrix[i][j]!=0 and matrix[i][j] != 1:
                raise ValueError("Macierz zawiera wartości różne od 1 i 0")

def is_adj_list(adj_list):
    num_of_rows=len(adj_list)

    for i in range(num_of_rows): # sprawdzenie czy lista jest w poprawnym formacie
        for j in adj_list[i]:
            if j > num_of_rows:
                raise ValueError("Niepoprawny format listy sąsiedztwa")

def is_inc_matrix(matrix):
    num_of_cols=len(matrix[0])
    num_of_rows=len(matrix)
    edge_indexes=[]

    for j in range(num_of_cols): # sprawdzenie czy macierz jest w poprawnym formacie
        edge_indexes.clear()
        for i in range(num_of_rows):
            if matrix[i][j]!=1 and matrix[i][j]!=0:
                raise ValueError("Macierz zawiera wartości różne od 1 i 0")
            if matrix[i][j]==1:
                edge_indexes.append(i)
        if len(edge_indexes) != 2:
            raise ValueError("Macierz nie jest macierzą incydencji")