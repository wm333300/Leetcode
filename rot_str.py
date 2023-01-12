#++++++++++++++++++++++++++++++++++
# rstr
# Wasam
#++++++++++++++++++++++++++++++++++

def rotateString(s, goal):
    rot = s[1:] + s[0]
    while rot != s:
        if rot == goal:
            return True
        else:
            rot = rot[1:] + rot[0]
    return False