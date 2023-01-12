#=============================
# nge

# By Wasam
#=============================

def nextGreaterElement(nums1, nums2):
    ans = []
    for elem in nums1:
        if elem == max(nums2[nums2.index(elem):]):
            ans.append(-1)
        else:
            for elem2 in nums2[nums2.index(elem):]:
                if elem2 > elem:
                    ans.append(elem2)
                    break
    return ans
            
        
        
        