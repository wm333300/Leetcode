#++++++++++++++++++++++++++++++++++
# rw
# Wasam
#++++++++++++++++++++++++++++++++++

def reverseWords(s):
    st = s.split(" ")
    st = [list(elem) for elem in st]
    for elem in st:
        elem.reverse()
    for elem in range(len(st)):
        st[elem] = "".join(st[elem])
    st = " ".join(st)
    return st

            