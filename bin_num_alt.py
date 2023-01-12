#++++++++++++++++++++++++++++++++++
# Binnumalt
# Wasam
#++++++++++++++++++++++++++++++++++

    
def hasAlternatingBits(n):
    def num2bin(num):
        ans = []
        while num!=0:
            ans.append(num%2)
            num = num//2
        ans.reverse()
        return ans
    ch = num2bin(n)
    for ind in range(len(ch)-1):
        if ch[ind] == ch[ind+1]:
            return False
    return True

def num2bin(num):
    ans = []
    while num!=0:
        ans.append(num%2)
        num = num//2
    ans.reverse()
    return ans

def isPowerofTwo(n):
    if n == 2 or n==0: return True
    if n%2 == 0: return isPowerofTwo(n//2)
    return False
    