#++++++++++++++++++++++++++++++++++
# arrparity
# Wasam
#++++++++++++++++++++++++++++++++++

def sortArrayByParity(nums):
    ev = []
    od = []
    for elem in nums:
        if elem % 2 == 0:
            ev.append(elem)
        else:
            od.append(elem)
    return ev + od