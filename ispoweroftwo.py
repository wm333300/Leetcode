#++++++++++++++++++++++++++++++++++
# binarynums
# Wasam
#++++++++++++++++++++++++++++++++++

import math

def isPowerOfTwo(n):
    return (round(math.log(n, 2), 6) % 1) == 0
    
def isPowerofTwo_2(n):
    if n == 2 or n==0 or n==1: return True
    elif n%2 == 0: return isPowerofTwo_2(n//2)
    else: return False
    
def isPowerOfTwo_3(n):
    print(math.floor(math.log(n, 2)), math.ceil(math.log(n, 2)))
    return ((math.floor(math.log(n, 2))) == (math.ceil(math.log(n, 2))))