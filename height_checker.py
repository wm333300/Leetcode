#++++++++++++++++++++++++++++++++++
# hc
# Wasam
#++++++++++++++++++++++++++++++++++

def kWeakestRows(mat, k):
    ans_dict = {elem : mat[elem] for elem in range(len(mat))}
    mat.sort
    ans = []
    for elem in mat:
        ans.append(list(ans_dict.keys())[list(ans_dict.values()).index[elem]])
    return [:k]