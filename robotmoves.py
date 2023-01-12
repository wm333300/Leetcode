#=============================
# intersec

# By Wasam
#=============================

def judgeCircle(moves):
    loc = [0,0]
    for elem in moves:
        if elem == "U":
            loc[1] += 1
        elif elem == "D":
            loc[1] -= 1
        elif elem == "R":
            loc[0] += 1
        else:
            loc[0] -= 1
    return loc == [0,0]