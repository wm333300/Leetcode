#=============================
# countBits
# By Wasam
#=============================

def countBits(n):
    def num_to_bin(num):
        fin_len = num // 2
        ans = []
        while num != 0:
            ans.append(num%2)
            num = num//2
        ans.reverse()
        return ans 
    fin_ans = []
    for elem in range(n+1):
        fin_ans.append(num_to_bin(elem).count(1))
    return fin_ans

def num_to_bin(num):
    fin_len = num // 2
    ans = []
    while num != 0:
        ans.append(num%2)
        num = num//2
    ans.reverse()
    return ans 