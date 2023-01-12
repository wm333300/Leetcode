#++++++++++++++++++++++++++++++++++
# findComplement
# Wasam
#++++++++++++++++++++++++++++++++++

def findComplement(num):
    
    def dec2bin(n):
        ans = []
        bit = 0
        while n != 0:
            ans.append(n%2)
            n = n//2
            bit+=1
        ans.reverse()
        return ans 
    
    def bin2dec(bin_n):
        bin_n.reverse()
        answer = 0
        for elem in range(len(bin_n)):
            answer += bin_n[elem] * 2 ** elem
        return answer
    
    bin_num = dec2bin(num)
    ind = 0
    while ind < len(bin_num):
        print(bin_num)
        if bin_num[ind] == 0:
            bin_num.pop(ind)
            bin_num.insert(ind, 1)
            ind += 1
        elif bin_num[ind] == 1:
            bin_num.pop(ind)
            bin_num.insert(ind, 0)
            ind += 1
        else:
            ind += 1
    return bin2dec(bin_num)

def dec2bin(n):
    ans = []
    bit = 0
    while n != 0:
        ans.append(n%2)
        n = n//2
        bit+=1
    ans.reverse()
    return ans
            
def bin2dec(bin_n):
    bin_n.reverse()
    answer = 0
    for elem in range(len(bin_n)):
        answer += bin_n[elem] * 2 ** elem
    return answer