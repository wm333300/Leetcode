#++++++++++++++++++++++++++++++++++
# vpii
# Wasam
#++++++++++++++++++++++++++++++++++

def validPalindrome_ii(s):
    s = list(s)
    def validPalindrome(s):
        a = []
        b = []
        s = list(s)
        if len(s) % 2 == 0:
            a = s[:len(s)//2]
            b = s[len(s)//2:]
        else:
            a = s[:len(s)//2]
            b = s[(len(s)//2)+1:]
        b.reverse()
        #print(a,b)
        return a == b
    for elem in range(len(s)):
        x = s[elem]
        del s[elem]
        if validPalindrome(s[:]):
            return True
        s.insert(elem, x)
    return False



    

  