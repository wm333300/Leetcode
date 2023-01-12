#++++++++++++++++++++++++++++++++++
# disnum
# Wasam
#++++++++++++++++++++++++++++++++++

def findDisappearedNumbers(nums):
    ans = {}
    ind = 0
    nums.sort()
    while ind < len(nums) - 1:
        if (nums[ind] != ind+1):
            ans[ind+1] = ind+1
            ind += 1
        else:
            ind += 1
    return list(ans.values())

def disnum(nums):
    ind = 0
    ans = []
    while ind < len(nums):
        if ind+1 not in nums:
            ans.append(ind+1)
            ind += 1
        else:
            ind+=1
    return ans

def disnum_2(nums):
    c_l = [elem+1 for elem in range(len(nums))]
    return list({elem for elem in c_l if elem not in nums})
    