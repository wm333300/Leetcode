#++++++++++++++++++++++++++++++++++
# bC
# Wasam
#++++++++++++++++++++++++++++++++++

def backspaceCompare(s, t):
    s = list(s)
    t = list(t)
    ind = 0
    while ind < len(s):
        if ind < len(s)-1:
            if s[ind] == "#":
                del s[ind-1]
                del s[ind-1] 
        if ind == len(s)-1:
            del s[-1]
            del s[-1]                     
        ind += 1
    ind2 = 0
    while ind2 < len(t):
        if ind2 < len(t)-1:
            if t[ind2] == "#":
                del t[ind2-1]
                del t[ind2-1]  
        if ind2 == len(t)-1:
            del t[-1]
            del t[-1]             
        ind2 += 1    
    return s, t

def backspaceCompare_2(s, t):
    s = list(s)
    t = list(t)
    s_1 = []
    t_1 = []
    ind1 = len(s)-1
    ind2 = len(t)-1
    while ind1 >= 0:
        if s[ind1] == "#":
            del s[ind1-1]
            del s[ind1-1]
        ind1 -= 1
    while ind2 >= 0:
        if t[ind2] == "#":
            del t[ind2-1]
            del t[ind2-1]
        ind -= 1    
    return s,t

          
def backspaceCompare_3(s, t):
    s = list(s)
    t = list(t)
    s_hash = s.count("#")
    t_hash = t.count("#")
    ind1 = 0
    while s_hash != 0:
        if ind1 > len(s)-1:
            ind1 = 0
            s_hash = s.count("#")
        elif s[ind1] == "#" and ind1 > 0:
            del s[ind1-1:ind1+1]
            ind1 = 0
            s_hash = s.count("#")
        elif s[ind1] == "#":
            del s[ind1-1:ind1+1]
            ind1 = 0
            s_hash = s.count("#")
        else:
            ind1 += 1
            s_hash = s.count("#")
    ind2 = 0
    while t_hash != 0:
        if ind2 > len(t)-1:
            ind2 = 0
            t_hash = t.count("#")
        elif t[ind2] == "#" and ind2 > 0:
            del t[ind2-1:ind2+1]
            ind2 = 0
            t_hash = t.count("#")
        elif t[ind2] == "#":
            del t[ind2-1:ind2+1]
            ind2 = 0
            t_hash = t.count("#")
        else:
            ind2 += 1
            t_hash = t.count("#")    
    s = "".join(s)
    t = "".join(t)
    print(s,t)
    return s==t