#=============================
# isHappy()
# By Wasam
#=============================


def digi_sum(n):
    if n == 0: return 0
    if (n % 10) == 0: return digi_sum(n/10)
    return n%10 + digi_sum(n-n%10)

def digi_sum_it(n):
    sum_of_dig = 0
    while n != 0:
        if (n % 10 == 0):
            n = n / 10
        else:
            sum_of_dig += n%10
            n -= n%10
    return sum_of_dig

def digi_sum_sq(num):
    sum_of_dig = 0
    while num != 0:
        if (num % 10 == 0):
            num = num / 10
        else:
            sum_of_dig += (num%10)**2
            num -= num%10
    return sum_of_dig

def isHappy(n):
    def digi_sum_sq(num):
        sum_of_dig = 0
        while num != 0:
            if (num % 10 == 0):
                num = num / 10
            else:
                sum_of_dig += (num%10)**2
                num -= num%10
        return sum_of_dig    
        curr_num = digi_sum_sq(n)
    stack = []
    while True:
        if curr_num == 1.0: break
        if curr_num in stack : break
        stack.append(curr_num)
        curr_num = digi_sum_sq(curr_num)
    return (curr_num == 1)