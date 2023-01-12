#=============================
# Excel Col
# By Wasam
#=============================

import math

def excel(columnNumber):
    check_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 
                  7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 
                  13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 
                  19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 0: 'Z'}
    answer = []
    remainder = (columnNumber%26)
    answer.append(check_dict[remainder])
    n_full = round(math.log(columnNumber,26))
    for elem in range(n_full):
        answer.append(check_dict[n_full])
    answer.reverse()
    return answer
        
        
def excel_2(n):
    check_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 
                  7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 
                  13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 
                  19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        
    ans = []
    while q != 0:
        r = q % 26
        ans.append(check_dict[r])
        q = q // 26
        ans.reverse()
    return ans

def dtb(n): 
    ans = []
    q = n // 2
    r = n % 2
    while q != 0:
        q = n // 2
        r = n % 2
        n = q
        ans.append(r)
    ans.reverse()
    return ans
    
    
def excel_to_num(columnTitle):
    dict_vals = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                 'Z': 26}
    lst_to_check = list(columnTitle)
    lst_to_check.reverse()
    ans = 0
    for elem in range(len(lst_to_check)):
        ans += (dict_vals[lst_to_check[elem]])*26**elem
    return ans 