#++++++++++++++++++++++++++++++++++
# as
# Wasam
#++++++++++++++++++++++++++++++++++

def all_subs(s):
    al = []
    for elem in range(len(s)+1):
        for elem2 in range(len(s)+1):
            if elem2 > elem:
                al.append(s[elem:elem2])
    al = list(filter(lambda x: ((len(s) % len(x) == 0) and len(x) != len(s)), al))
    c_l = []
    for elem in al:
        check = []
        while len(check) < len(s)//len(elem):
            check.append(elem)
        c_l.append("".join(check))
    for elem in c_l: 
        if elem == s: return True
    return False

def all_subs_2(s):
    al = list(filter(lambda x: ((len(s) % len(x) == 0) and len(x) != len(s)), 
                     [[s[elem:elem2] for elem2 in range(len(s)+1)] for elem in range(len(s)+1)]))
    c_l = []
    for elem in al:
        check = []
        while len(check) < len(s)//len(elem):
            check.append(elem)
        c_l.append("".join(check))
    for elem in c_l: 
        if elem == s: return True
    return False    