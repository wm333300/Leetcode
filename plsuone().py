#=============================
# plusOne
# By Wasam
#=============================

def plusOne(digits):
    return list(map(int, list(str(int(''.join(list(map(str, digits)))) + 1))))