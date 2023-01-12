#++++++++++++++++++++++++++++++++++
# mr
# Wasam
#++++++++++++++++++++++++++++++++++


def matrixReshape(mat, r, c):
    empty_lst = []
    ans = [[0 for elem in range(c)] for elem in range(r)]
    if ((len(mat)*len(mat[0])) != r*c): return mat
    for elem in mat:
        for elem2 in elem:
            empty_lst.append(elem2)
    empty_lst.reverse()
    for e1 in range(len(ans)):
        for e2 in range(len(ans[e1])):
            ans[e1][e2] = empty_lst.pop()
    return ans 
    
    
    