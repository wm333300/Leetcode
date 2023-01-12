#++++++++++++++++++++++++++++++++++
# unc
# Wasam
#++++++++++++++++++++++++++++++++++

def uncommonFromSentences(s1, s2):
    s1_lst = s1.split(" ")
    s2_lst = s2.split(" ")
    ans = []
    for elem in s1_lst:
        if elem not in s2_lst:
            ans.append(elem)
    for elem in s2_lst:
        if elem not in s1_lst:
            ans.append(elem)    
    return ans
        