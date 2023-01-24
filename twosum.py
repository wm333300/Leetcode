# Python twosum

v1 = ([2,7,11,15], 9)
v2 = ([3,2,4], 6)

def twosum(nums, target):
    curr_val = 0
    i = 0
    ans = []
    while i < len(nums)-1:
        k = i+1
        while k < len(nums):
            print(i,k)
            if ((nums[i]+nums[k]) == target):
                ans += [i,k]
            k += 1
        i += 1
    return ans