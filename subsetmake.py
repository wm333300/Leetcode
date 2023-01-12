#++++++++++++++++++++++++++++++++++
# sub
# Wasam
#++++++++++++++++++++++++++++++++++

def findShortestSubArray(nums):
    pass

def los(l):
    ans = []
    ind = len(l)
    while ind > -1:
        sub = []
        for elem in l[:ind]:
            sub.append(elem)
        ans.append(sub)
        ind -= 1
    return ans

def los(l):
    ans = []
    ind1 = 0
    while ind1 < len(l):
        ind2 = ind1 + 1
        while ind2 <= len(l):
            print(ind1, ind2)
            ans.append(l[ind1:ind2])
            ind2 += 1
        ind1 += 1
    ans = sorted(ans, key = len)
    return ans

        
        