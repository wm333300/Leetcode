#=============================
# rem_dups()
# By Wasam
#=============================

def rem_dups(st):
    ind = 0
    ans = []
    while ind < len(st):
        if st[ind] not in st[ind+1:]:
            ans.append(st[ind])
            ind += 1
        else:
            ind += 1
    return ans
    
