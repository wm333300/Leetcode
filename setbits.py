#++++++++++++++++++++++++++++++++++
# setbits
# Wasam
#++++++++++++++++++++++++++++++++++

import math


def countPrimeSetBits(left, right):
    def is_prime(n):
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i) == 0:
                return False
        return True
    
    def num2bin(num):
        ans = []
        while num!=0:
            ans.append(num%2)
            num = num//2
        ans.reverse()
        return ans
    a_dict = {}
    for elem in range(left,right):
        a_dict[elem] = num2bin(elem)
    count = 0
    for elem in a_dict.values():
        if is_prime(elem.count(1)):
            count += 1
    return count