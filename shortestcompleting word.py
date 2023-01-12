#++++++++++++++++++++++++++++++++++
# scw
# Wasam
#++++++++++++++++++++++++++++++++++

def shortestCompletingWord(licensePlate, words):
    lp = [elem for elem in licensePlate.lower() if elem in "abcdefghijklmnopqrstuvwxyz"]
    lp_dict = {elem:lp.count(elem) for elem in lp}
    listone = []
    def checkex(a_dict,b):
        for elem in lp_dict:
            if b.count(elem) != lp_dict[elem]:
                return False
        return True        
    for elem in words:
        if checkex(lp_dict, elem):
            listone.append(elem)
    listone = sorted(listone, key = len)
    return listone[0]
            
