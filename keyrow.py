#++++++++++++++++++++++++++++++++++
# sdn
# Wasam
#++++++++++++++++++++++++++++++++++

def findWords(words):
    def ainkeyb(a,b,c,d):
        b_chk = True
        c_chk = True
        d_chk = True
        for elem in list(a):
            if elem not in b: b_chk = False
            if elem not in c: c_chk = False
            if elem not in d: d_chk = False
        return (b_chk or c_chk or d_chk)
    ans = []
    for elem in words:
        if ainkeyb(elem.lower(), "qwertyuiop", "asdfghjkl", "zxcvbnm"):
            ans.append(elem)
    return ans


def ainb(a,b,c,d):
    b_chk = True
    c_chk = False
    d_chk = False
    for elem in list(a):
        if elem not in b: b_chk = False
    return (b_chk or c_chk or d_chk)
