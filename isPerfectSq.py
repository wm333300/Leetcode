# Wasam isPerfectSquare

n1 = 0
n2 = 1
n3 = 2147483647

    
def isPerfectSquare(num):
    sub = 1
    while num>=1:
        num -= sub
        sub += 2
    if num == 0: return True
    else: return False