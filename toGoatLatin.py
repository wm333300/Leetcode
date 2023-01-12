#++++++++++++++++++++++++++++++++++
# tGL
# Wasam
#++++++++++++++++++++++++++++++++++

def toGoatLatin(sentence):
    st = sentence.split(" ")
    ans = []
    for elem in range(len(st)):
        s = ""
        if st[elem][0] not in "aeiouAEIOU":
            s += st[elem][1:] + st[elem][0] + "ma" + ("a"*(elem+1))
        else:
            s += st[elem] + "ma" + ("a"*(elem+1))
        ans.append(s)
    ans = " ".join(ans)
    return ans
        
            