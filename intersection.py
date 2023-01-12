#=============================
# intersec

# By Wasam
#=============================

def intersection(nums1, nums2):
    ans = []
    def rem_dups(lst):
        i = 0
        fin_lst = []
        while i < len(lst):
            if (lst[i] not in lst[i+1:]) and (lst[i] not in fin_lst):
                fin_lst.append(lst[i])       
            i += 1
        return fin_lst
    if len(nums1) > len(nums2):
        ans = list(filter(lambda x: x in nums1, nums2))
    else:
        ans = list(filter(lambda x: x in nums1, nums2))
    ans = rem_dups(ans)
    return ans