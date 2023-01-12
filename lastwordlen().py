#=============================
# Last Word Length
# By Wasam
#=============================

def lengthOfLastWord(s):
    x = s.split(" ")
    return len([elem for elem in x if elem != ""][-1])