#++++++++++++++++++++++++++++++++++
# sabpii
# Wasam
#++++++++++++++++++++++++++++++++++

def binaryGap(n):
    def num2bin(num):
        ans = []
        while num != 0:
            ans.append(num%2)
            num = num //2
        ans.reverse()
        return ans
    bin_rep = num2bin(n)
    ind = bin_rep.index(1) + 1
    fin_ind = 0
    while ind < len(bin_rep):
        if bin_rep[ind] == 1:
            fin_ind = ind - bin_rep.index(1)
            break
        else:
            ind += 1
    print(bin_rep)
    return fin_ind 