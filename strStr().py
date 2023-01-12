#=============================
# Str str
# By Wasam
#=============================

def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    elif needle == "":
        return 0
    else:
        return haystack.index(needle)