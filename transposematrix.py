#++++++++++++++++++++++++++++++++++
# transpose
# Wasam
#++++++++++++++++++++++++++++++++++

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = [[0 for elem2 in matrix] for elem in matrix[0]]
    for elem in range(m):
        for elem2 in range(n):
            ans[elem2][elem] = matrix[elem][elem2]
    return ans