#++++++++++++++++++++++++++++++++++
# cbs
# Wasam
#++++++++++++++++++++++++++++++++++


def find_deg(arr):
    ans_dict = {elem:0 for elem in arr}
    for elem in arr:
        ans_dict[elem] += 1 
    return max(list(ans_dict.values())) 
        
        
def los(l):
    ans = {}
    ind1 = 0
    while ind1 < len(l):
        ind2 = ind1 + 1
        while ind2 <= len(l):
            ans.append(l[ind1:ind2])
            ind2 += 1
        ind1 += 1
    ans = sorted(ans, key = len)
    return ans

def findShortestSubArray(nums):
    def find_deg(arr):
        ans_dict = {elem:0 for elem in arr}
        for elem in arr:
            ans_dict[elem] += 1 
        return max(list(ans_dict.values())) 
            
            
    def los(l):
        ans = []
        ind1 = 0
        while ind1 < len(l):
            ind2 = ind1 + 1
            while ind2 <= len(l):
                ans.append(l[ind1:ind2])
                ind2 += 1
            ind1 += 1
        ans = sorted(ans, key = len)
        return ans    
    num_lst = los(nums)
    main_deg = find_deg(nums)
    deg_lst = [(find_deg(elem), len(elem)) for elem in num_lst]
    deg_lst = [elem for elem in deg_lst if elem[0] == main_deg]
    return min(deg_lst)[1]