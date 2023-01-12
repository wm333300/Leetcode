#=============================
# sqrt(x)
# By Wasam
#=============================

import time

def mySqrt(x):
    c = 0
    guess = x // 2
    fx = guess
    while (fx > 0.9):
        fx = (guess *guess)-x
        c += 1
        guess = guess - (((guess*guess) - x)/(2*(guess)))
    return int(guess) , c


    
  
def bsr(number):
    start = 0
    end = number
    mid = 0
    ans = 0
    c = 0
    while (start <= end):
        mid = (start + end) / 2
        if (mid * mid) == number:
            ans = mid
            break
        elif (mid *mid) < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    incr = 0.1
    ind = 0
    while ind < 1:
        while (ans * ans <= number):
            ans += incr
            c += 1
        ind += 1
        ans = ans - incr
        incr = incr / 10
    return int(ans), c
  
n = 2**31 - 1
  
print(bsr(n))
print(mySqrt(n))
print(time.process_time())