#++++++++++++++++++++++++++++++++++
# Baseball Game
# Wasam
#++++++++++++++++++++++++++++++++++

def calPoints(ops):
    record = []
    for elem in ops:
        if elem == "D":
            record.append(record[-1]*2)
        elif elem == "+":
            record.append(record[-1] + record[-2])
        elif elem == "C":
            record.pop()
        else:
            record.append(int(elem))
    print(record)
    return sum(record)

