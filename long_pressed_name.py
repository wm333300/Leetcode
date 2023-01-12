#++++++++++++++++++++++++++++++++++
# lpn
# Wasam
#++++++++++++++++++++++++++++++++++

def isLongPressedName(name, typed):
    ans = []
    check_ans = []
    for elem in name:
        if typed.count(elem) >= name.count(elem):
            ans.append(True)
            check_ans.append(elem)
        else:
            check_ans.append(elem)
            ans.append(False)
    def rem_dups(alst):
        ans = []
        for elem in range(len(alst)):
            if alst[elem] not in alst[elem+1:]:
                ans.append(alst[elem])
        return ans
    check_ans = "".join(check_ans)
    n_rd = rem_dups(name)
    t_rd = rem_dups(typed)
    print(check_ans, n_rd, t_rd, ans)
    return all(ans) and (check_ans == name) and (t_rd == n_rd)

def isLongPressedName_2(name, typed):
    pass

def rem_dups_2(alst):
    ind = 0
    k = 1
    ans = []
    while ind+k < len(alst): 
        if ind+k >= len(alst)-2:
            if alst [ind] == alst[ind-1]:
                ind += 1
                break
            else:
                ans.append(alst[ind+1])
                ind += 1
                break
        if alst[ind] == alst[ind+k]:
            k += 1
        if alst[ind] != alst[ind+k]:
            ans.append(alst[ind])
            ind += k
            print(ind)
            k = 1
    return ans
            