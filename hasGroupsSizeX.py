#++++++++++++++++++++++++++++++++++
# hGSX
# Wasam
#++++++++++++++++++++++++++++++++++

def hasGroupsSizeX(deck):
    deck.sort()
    def create_subs(al, n):
        ans = []
        ind = 0
        if n==0: return []
        while ind < len(al):
            ans.append(al[ind:ind+n])
            ind += n 
        return ans
    def all_equal(l):
        m = l[0]
        for elem in l:
            if elem != m:
                return False
        return True    
    curr = []
    if len(deck) == 2:
        if all_equal(deck): return True
        else: return False
    for elem in range(len(deck)):
        if elem >= 2 and (len(deck)%elem == 0):
            curr.append(create_subs(deck, elem))
    main = [[[all_equal(i), len(i)] for i in k] for k in curr]
    #print(main)  
    a = []
    for elem in main:
        if all_equal(elem) and (elem[0][0] != False):
            a.append(True)
        else:
            a.append(False)
    if True in a: return True
    else: return False
    
def all_equal(l):
    m = l[0]
    for elem in l:
        if elem != m:
            return False
    return True   

def create_subs(al, n):
    ans = []
    ind = 0
    if n==0: return []
    while ind < len(al):
        ans.append(al[ind:ind+n])
        ind += n 
    return ans