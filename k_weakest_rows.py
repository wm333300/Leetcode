#++++++++++++++++++++++++++++++++++
# hc
# Wasam
#++++++++++++++++++++++++++++++++++

def kWeakestRows(mat, k):
    ans = [(elem, mat[elem].count(1)) for elem in range(len(mat))]
    ans = sorted(ans, key = lambda x: x[1])
    return [elem[0] for elem in ans][:k]