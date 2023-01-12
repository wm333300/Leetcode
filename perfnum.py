#++++++++++++++++++++++++++++++++++
# cpn
# Wasam
#++++++++++++++++++++++++++++++++++

def checkPerfectNumber(num):
    ch = 1
    if num%2 == 0: ch = 2
    elif num%3 == 0: ch = 3
    elif num%5 == 0: ch = 5
    elif num%7 == 0: ch = 7
    else: 
        ch = 1
    return (sum(list(filter(lambda x: num%x == 0, [elem+1 for elem in range((num//ch))]))) == num)

def cpn(num):
    ind = 1
    ans = 0
    while ind <= num//2:
        if num%ind == 0:
            ans += ind
            ind += 1
        else:
            ind += 1
    return ans == num

def cpn_2(num):
    ind = 0
    ans = []
    while ind <= 20:
        if ind == 1:
            ans.append(((2**(ind)) * ((2**((ind) + 1)-1))))
        ans.append(((2**(2*ind)) * ((2**((2*ind) + 1)-1))))
        ind += 1
    return ans
        
