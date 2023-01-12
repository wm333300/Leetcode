#=============================
# intersec

# By Wasam
#=============================

def findDisappearedNumbers(nums):
    def rem_dups(lst):
        i = 0
        fin_lst = []
        while i < len(lst):
            if (lst[i] not in lst[i+1:]) and (lst[i] not in fin_lst):
                fin_lst.append(lst[i])       
            i += 1
        return fin_lst    
    ans = []
    init_num_length = len(nums)
    i = 1
    nums.sort()
    nums = rem_dups
    while i < init_num_length:
        if i not in nums:
            ans.append(i)
        i += 1
    return ans

def rem_dups(lst):
    i = 0
    fin_lst = []
    while i < len(lst):
        if (lst[i] not in lst[i+1:]) and (lst[i] not in fin_lst):
            fin_lst.append(lst[i])       
        i += 1
    return fin_lst