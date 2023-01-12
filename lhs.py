#++++++++++++++++++++++++++++++++++
# lhs
# Wasam
#++++++++++++++++++++++++++++++++++

def findLHS(nums):
    for ind1 in nums:
        for ind2 in nums:
            if ind1<ind2:
                print(nums[ind1:ind2])
    