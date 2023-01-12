#=============================
# reverseVowels()
# By Wasam
#=============================

def reverseVowels(s):
    v_lst = [elem for elem in s if elem in "aeiouAEIOU"]
    s = list(s)
    for elem2 in range(len(s)):
        if s[elem2] in "aeiouAEIOU":
            s[elem2] = v_lst.pop()
    s = "".join(s)
    return s
