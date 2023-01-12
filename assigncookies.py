#++++++++++++++++++++++++++++++++++
# Assign Cookies
# Wasam
#++++++++++++++++++++++++++++++++++

def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    print(g)
    def c_true(a, lst):
        for elem in lst:
            if elem >= a:
                return True
        return False
    ind = 0
    ans = []
    while ind < len(g):
        if (c_true(g[ind], s)):
            ans.append(g[ind])
            #del s[s.index(g[ind])]
            ind += 1
        else:
            ind += 1
    return len(ans)