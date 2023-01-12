#++++++++++++++++++++++++++++++++++
# isOneBitCharacter
# Wasam
#++++++++++++++++++++++++++++++++++

def isOneBitCharacter(bits):
    ans = []
    ind = 0
    while ind < len(bits):
        if (bits[ind] == 0):
            ans.append([bits[ind]])
            ind += 1
        elif (bits[ind] == 1):
            ans.append([bits[ind:ind+2]])
            ind += 2
        else:
            return False
    return ans.pop() == [0]
            