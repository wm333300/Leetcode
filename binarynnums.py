#++++++++++++++++++++++++++++++++++
# binarynums
# Wasam
#++++++++++++++++++++++++++++++++++

def dec2bin(num):
    ans = [0 for elem in range(64)]
    bit = 0
    while num != 0:
        ans[bit] = num%2
        num = num//2
        bit+=1
    return ans