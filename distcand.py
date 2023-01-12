#++++++++++++++++++++++++++++++++++
# Distribute Candy
# Wasam
#++++++++++++++++++++++++++++++++++

def distributeCandies(candyType):
    n = len(candyType)//2
    diff_types = []
    for elem in candyType:
        if elem not in diff_types:
            diff_types.append(elem)
    return min(len(diff_types), n)