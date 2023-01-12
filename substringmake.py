#++++++++++++++++++++++++++++++++++
# sub
# Wasam
#++++++++++++++++++++++++++++++++++

def subs(s):
    ans = []
    for elem in range(len(s)):
        for elem2 in range(len(s)):
            ans.append(s[elem:elem2])
    ans = [elem for elem in ans if elem != ""]
    return ans

def count_zeros_and_ones(s):
    zeros = 0
    ones = 0
    for elem in s:
        if elem == "0":
            zeros += 1
        if elem == "1":
            ones += 1
    return zeros == ones

def countBinarySubstrings(s):
    sub_s = subs(s)
    count = 0
    for elem in sub_s:
        if count_zeros_and_ones(elem):
            count += 1
    return count

        
        