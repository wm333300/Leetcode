#++++++++++++++++++++++++++++++++++
# Contains nearby duplicate
# Wasam
#++++++++++++++++++++++++++++++++++

def lst_cont_dup(alst,b):
    ind = 0
    curr = 0
    while ind < len(alst):
        curr = alst[ind]
        for elem in alst[ind+1:ind+b+1]:
            if elem == curr:
                return True
        ind += 1
    return False

def lst_cont_dup_2(alst,b):
    ind = 0
    curr = 0
    while ind < len(alst):
        curr = alst[ind]
        if alst[ind] in alst[ind+1:ind+1+b]:
            return True
        ind += 1
    return False

def create_dup(alon, k):
    ind = 0
    ans = []
    while ind < (len(alon)):
        ans.append(alon[ind:ind+k+1])
        ind += 1
    return ans

def containsNearbyDuplicate(nums, k):
    pass
