#++++++++++++++++++++++++++++++++++
# b7
# Wasam
#++++++++++++++++++++++++++++++++++

def base_7(num):
    check = str(num)[0] == "-"
    k = abs(num)
    ans = []
    if k == 0: return str(0)
    while k != 0:
        ans.append(k % 7)
        k = k // 7
    ans.reverse()
    if check: return "-" + "".join([str(elem) for elem in ans])
    return "".join([str(elem) for elem in ans])
        