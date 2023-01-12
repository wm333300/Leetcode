#=============================
# recursion
# By Wasam
#=============================


def sum_of_list(alon):
    if alon == []: return 0
    return alon[0] + sum_of_list(alon[1:]) 

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1) 
    
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def sum_series(n):
    if n <= 0: return n
    return n + sum_series(n-2)

def sum_harmonic(n):
    if n == 1: return 1
    return 1/n + sum_harmonic(n-1)

def sum_harmonic_it(n):
    ans = 0
    while n != 0:
        ans += 1/n
        n -= 1
    return ans

def power(a,b):
    if b == 0: return 1
    return a * power(a, b-1)

def sum_of_l_ext(li):
    if li == []: return 0
    if type(li[0]) == list: return sum_of_l_ext(li[0]) + sum_of_l_ext(li[1:])
    return li[0] + sum_of_l_ext(li[1:])

def digi_sum(n):
    if n == 0: return 0
    if (n % 10) == 0: return digi_sum(n/10)
    return n%10 + digi_sum(n-n%10)

def digi_sum_it(n):
    sums = 0
    while n >= 0:
        if n == 0:
            sums += 0
            break
        if n%10 == 0: 
            n = n/10
        sums += n%10
        n -= n%10
    return sums
        

def gcd(a,b):
    def lcm(a,b,n):
        if (a * n) % b == 0: return a * n
        return lcm(a,b,n+1)
    return a*b / (lcm(a,b,1))

# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php#EDITOR

def fib_mem(n, memo = {}):
    if (n in memo): return memo[n]
    if (n <= 2): return 1
    memo[n] = fib_mem(n-1, memo) + fib_mem(n-2, memo)
    return memo[n]

def grid_trav(m,n, memo = {}):
    key = "{0},{1}".format(m,n)
    if (key in memo): return memo[key]
    if (m == 0) or (n == 0): return 0
    if (m == 1) or (n == 1): return 1
    if (m == 2): return n
    if (n == 2): return m
    memo[key] = grid_trav(m-1, n) + grid_trav(m, n-1)
    return memo[key]



def num_to_ex(num):
    ch_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
               9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P',
               17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 
               25: 'Y', 0: 'Z'}
    ans = []
    while num != 0:    
        if num == 26:
            ans.append(ch_dict[0])
            break
        if (num%26 == 0): 
            num = ((num//26) - 1) * 26
        ans.append(ch_dict[num%26])
        num = num//26
    ans.reverse()
    return ans

def bin_(n):
    def num_to_bin(num):
        fin_len = num // 2
        ans = []
        while num != 0:
            ans.append(num%2)
            num = num//2
        ans.reverse()
        return ans    
    def list_to_bin(alst):
        ans = 0
        for elem in range(len(alst)):
            ans += alst[elem]*2**elem
        return ans    
    bin_list = num_to_bin(n)
    bin32 = [0 for elem in range(32)]
    ind = 0
    bin32[32-len(bin_list):] = bin_list
    return list_to_bin(bin32)


    
    

    
