#++++++++++++++++++++++++++++++++++
# int
# Wasam
#++++++++++++++++++++++++++++++++++

def intersect(nums1, nums2):
     nums1.sort()
     nums2.sort()
     a = [nums1[elem] for elem in range(len(nums1)) 
          if nums1[elem] in nums2]
     b = [nums2[elem] for elem in range(len(nums2)) 
          if nums2[elem] in nums1]     
     if len(a) < len(b):
          return a
     else:
          return b