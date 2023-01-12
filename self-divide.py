#++++++++++++++++++++++++++++++++++
# sdn
# Wasam
#++++++++++++++++++++++++++++++++++

def selfDividingNumbers(left, right):
    
    def extract_dig(n):
        ans = []
        while n != 0:
            if n%10 == 0:
                ans.append(0)
                n = n // 10
            else:
                ans.append(n%10)
                n = (n-n%10)//10
        ans.reverse()
        return ans   
    
    def check_division(alst, anum):
        for elem in alst:
            if elem == 0: return False
            if anum % elem != 0: 
                return False
        return True    
    
    ans = [elem for elem in range(left,right+1)]
    fin = []
    ex_dig_el = []
    for elem in range(len(ans)):
        ex_dig_el = extract_dig(ans[elem])
        if check_division(ex_dig_el, ans[elem]):
            fin.append(ans[elem])
    return fin
        


def extract_dig(n):
    ans = []
    while n != 0:
        if n%10 == 0:
            ans.append(0)
            n = n // 10
        else:
            ans.append(n%10)
            n = (n-n%10)//10
    ans.reverse()
    return ans
    
def check_division(alst, anum):
    for elem in alst:
        if anum % elem != 0: 
            return False
    return True