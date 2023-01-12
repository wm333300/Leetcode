#=============================
# issubsequence()
# By Wasam
#=============================

def isSubsequence(s, t):
    s_init = s
    check_stack = []
    curr_check = ""
    ind = 0
    while ind < len(t):
        if s == "": break
        curr_check = s[0]
        if curr_check == t[ind]:
            print(ind, "hi",s)
            check_stack.append(curr_check)
            s = s[1:]
            ind += 1
        else:
            ind += 1
    check_stack = "".join(check_stack)
    return check_stack, s_init