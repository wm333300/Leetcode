#=============================
# firstUniqChar
# By Wasam
#=============================

def firstUniqChar(s):
    ind = 0
    st = []
    while ind < len(s)-1:
        print(s[ind+1:],ind, s[ind])
        if s[ind] in s[ind+1:]:
            
            ind += 1
        else:
            st.append(ind)
            ind += 1
    if st == []: return -1
    return st[0]
            
            
def rem_dups(st):
    ind = 0
    ans = []
    while ind < len(st):
        if st[ind] in st[ind+1:]:
            ind += 1
        else:
            ans.append(st[ind])
            ind += 1
    return ans

def count_occurence(elem, strs):
    count = 0
    for e in strs:
        if e == elem:
            count += 1
    return count
            
def firstUniqChar_2(s):
    def rem_dups(st):
        ind = 0
        ans = []
        while ind < len(st):
            if st[ind] in st[ind+1:]:
                ind += 1
            else:
                ans.append(st[ind])
                ind += 1
        return ans
    
    def count_occurence(elem, strs):
        count = 0
        for e in strs:
            if e == elem:
                count += 1
        return count    

    uniqlst = rem_dups(s)
    dic = {x: count_occurence(x, s) for x in uniqlst}
    ans = []
    for elem in s:
        if dic[elem] == 1:
            ans.append(elem)
    if ans == []: return -1
    return s.index(ans[0])
    