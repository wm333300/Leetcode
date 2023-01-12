#=============================
# Romannumerals
# By Wasam
#=============================

import csv
import pandas as pd

df = pd.read_csv(r'C:\Users\LENOVO\Desktop\leetcode\romannumerals.csv')
lor = df['Roman'].tolist()
loi = df['Integer'].tolist()

def romanToInt(s):
    numbers_dict = { "M" : 1000,
                     "D" : 500,
                     "C" : 100,
                     "L" : 50,
                     "X" : 10,
                     "V" : 5,
                     "I" : 1
    }
    ans = 0
    ind = 0
    q_string = list(s)
    check = True
    while (ind < len(q_string)):
        if (q_string[ind] == "C"):
            if (ind == len(q_string) - 1):
                ans += 100
                ind += 1             
            elif (q_string[ind+1] == "M"):
                    ans += 900
                    ind += 2
            elif (q_string[ind+1] == "D"):
                    ans += 400
                    ind += 2
            else:
                ans += 100
                ind += 1
        elif (q_string[ind] == "X"):
            if (ind == len(q_string) - 1):
                ans += 10
                ind += 1            
            elif (q_string[ind+1] == "C"):
                ans += 90
                ind += 2
            elif (q_string[ind+1] == "L"):
                ans += 40
                ind += 2
            else:
                ans += 10
                ind += 1  
        elif (q_string[ind] == "I"):
            if (ind == len(q_string) - 1):
                ans += 1
                ind += 1
            elif (q_string[ind+1] == "X"):
                ans += 9
                ind += 2
            elif (q_string[ind+1] == "V"):
                ans += 4
                ind += 2
            else:
                ans += 1
                ind += 1 
        else: 
            if (q_string[ind] == "M"):
                ans += 1000
                ind += 1
            elif (q_string[ind] == "D"):
                ans += 500
                ind += 1
            elif (q_string[ind] == "L"):
                ans += 50
                ind += 1
            elif (q_string[ind] == "V"):
                ans += 5
                ind += 1
            elif (q_string[ind] == "I"):
                ans += 1    
                ind += 1         
            else:
                ind += 1
    return ans

x = list(map(romanToInt, lor[0:3999]))

print(x == loi[:3999])
