#++++++++++++++++++++++++++++++++++
# hammdist
# Wasam
#++++++++++++++++++++++++++++++++++

def dec2bin(num):
    ans = [0 for elem in range(32)]
    bit = 0
    while num != 0:
        ans[bit] = num%2
        num = num//2
        bit+=1
    return ans

def hammdist(x, y):
    def dec2bin(num):
        ans = [0 for elem in range(32)]
        bit = 0
        while num != 0:
            ans[bit] = num%2
            num = num//2
            bit+=1
        return ans    
    
    x = dec2bin(x)
    y = dec2bin(y)
    count = 0
    for elem in range(32):
        if (x[elem] != y[elem]):
            count += 1
    return count
        
        
        