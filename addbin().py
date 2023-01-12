#=============================
# addbin()
# By Wasam
#=============================

def addBinary(a, b):
    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    a.reverse()
    b.reverse()
    def bin_conv(num):
        ind = 0
        while ind < len(num):
            num[ind] = num[ind] * (2**ind)
            ind += 1
        return sum(num)
    a = bin_conv(a)
    b = bin_conv(b)
    return str(bin(a + b))[2:]