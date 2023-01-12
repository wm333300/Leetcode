#=============================
# climbStairs()
# By Wasam
#=============================


def climbStairs(n):
    if n == 1:
        return 1
    elif n== 0:
        return 1
    else:
        return climbStairs(n-2) + climbStairs(n-1)
    
def climbStairs_it(n):
    ind = 0
    a = 0
    b = 1
    t = 0
    while ind < n:
        t = a + b
        a = b 
        b = t
        ind += 1
    return b
        
        
        