#++++++++++++++++++++++++++++++++++
# revlet
# Wasam
#++++++++++++++++++++++++++++++++++

def reverseOnlyLetters(s):
    lets = []
    ans = []
    for elem in s:
        if elem.isalpha():
            lets.append(elem)
            ans.append("|")
        else:
            ans.append(elem)
    lets.reverse()
    print(ans)
    for elem in ans:
        if elem == "|":
            ans[ans.index(elem)] = lets[0]
            del lets[0]
    ans = "".join(ans)
    return ans