#=============================
# revstr
# By Wasam
#=============================

def reverseString(s):
    ind = len(s)-1
    init_length = len(s)
    while ind > -1:
        s.append(s[ind])
        ind -= 1
    s = s[init_length:]
   