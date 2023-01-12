#=============================
# hex
# By Wasam
#=============================

def toHex(num):
    pass

def htd(st):
    ch_d = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
            "a": 10, "b": 11, "c": 12, "d": 13, "e" : 14, "f" : 15}
    st = list(st)
    ans = 0
    for elem in range(len(st)):
        ans += ch_d[st[elem]] * 16 ** elem
    return ans
    