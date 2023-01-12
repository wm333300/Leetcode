#=============================
# Anagram
# By Wasam
#=============================

def isAnagram(s, t):
    s_sorted = list(s)
    t_sorted = list(t)
    s_sorted.sort()
    t_sorted.sort()
    return (s_sorted == t_sorted)