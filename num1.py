#=============================
# num1
# By Wasam
#=============================

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    return list(str(bin(n))).count("1")