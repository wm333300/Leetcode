#++++++++++++++++++++++++++++++++++
# fr
# Wasam
#++++++++++++++++++++++++++++++++++

def findRestaurant(list1, list2):
    ans = {elem: (list1.index(elem)+ list2.index(elem)) for elem in list1 if elem in list2}
    print(ans.values())
    a_l = []
    for elem in list(ans.values()):
        if elem == min(ans.values()):
            a_l.append(list(ans.values()).index(elem))
    return [list(ans.keys())[elem] for elem in a_l]
            