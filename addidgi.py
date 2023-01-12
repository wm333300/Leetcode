#=============================
# adddidgi
# By Wasam
#=============================

def addDigits(num):
    def digi_sum_it(n):
        sums = 0
        while n >= 0:
            if n == 0:
                break
            if n%10 == 0: 
                n = n/10
            sums += n%10
            n -= n%10
        return sums
    while (num // 10) != 0:
        num = digi_sum_it(num)
    return num