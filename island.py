#++++++++++++++++++++++++++++++++++
# islandPerimeter
# Wasam
#++++++++++++++++++++++++++++++++++

def islandPerimeter(grid):
    def check_single_row(row):
        count = 0
        if len(row) == 1 and row[0] == 1:
            count += 2
            return count
        for elem in range(len(row)):
            if (row[elem] == 1) and ((elem == 0) or (elem == (len(row) - 1))):
                count += 1
            if (row[elem] == 1)  and (elem != (len(row) - 1)) and (row[elem+1] == 0):
                count += 1
            if (row[elem] == 1)  and (elem != 0) and (row[elem-1] == 0):
                count += 1
        return count  
    def mat_tr(mat):
        r = len(mat)
        c = len(mat[0])    
        tr = []
        ind1 = 0 
        if r == c:
            tr = [[mat[elem][el2] for elem in range(c)] for el2 in range(r)]
        if r != c:
            tr = [[mat[elem][el2] for elem in range(r)] for el2 in range(c)]
        return tr    
    r = len(grid)
    c = len(grid[0])
    grid_transpose = mat_tr(grid)
    fin_count = 0
    for elem in grid:
        fin_count += check_single_row(elem)
    for elem in grid_transpose:
        fin_count += check_single_row(elem)
    return fin_count

def check_single_row(row):
    count = 0
    for elem in range(len(row)):
        if (row[elem] == 1) and ((elem == 0) or (elem == len(row) - 1)):
                count += 1
        if (row[elem] == 1) and (row[elem+1] == 0) and (elem != len(row) - 1):
            count += 1
        if (row[elem] == 1) and (row[elem-1] == 0) and (elem != 0):
            count += 1
    return count


def mat_tr(mat):
    r = len(mat)
    c = len(mat[0])    
    tr = []
    ind1 = 0 
    if r == c:
        tr = [[mat[elem][el2] for elem in range(c)] for el2 in range(r)]
    if r != c:
        tr = [[mat[elem][el2] for elem in range(r)] for el2 in range(c)]
    return tr

                
        
            
