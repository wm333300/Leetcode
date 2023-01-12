#++++++++++++++++++++++++++++++++++
# mcost
# Wasam
#++++++++++++++++++++++++++++++++++

def minCostClimbingStairs(cost):
    ind0 = 0
    cost_0 = cost[ind0]
    while ind0 < len(cost)-2: 
        if cost[ind0+1] >= cost[ind0+2]:
            cost_0 += cost[ind0+2]
            ind0 += 2
        else:
            cost_0 += cost[ind0+1]
            ind0 += 1
    ind1 = 1
    cost_1 = cost[ind1]
    while ind1 < len(cost)-2:
        if cost[ind1+1] >= cost[ind1+2]:
            cost_1 += cost[ind1+2]
            ind1 += 2
        else:
            cost_1 += cost[ind1+1]
            ind1 += 1   
    cost_skip2 = sum([cost[elem] for elem in range(0,len(cost),2)])
    return (min(cost_0, cost_1, cost_skip2))

def minCostClimbingStairs_2(cost):
    x_count = 0
    y_count = 0
    lst = []
    for elem in range(len(cost)):
        elem.append(1)


def minCostClimbingStairs_arjun(cost):
    size = len(cost)
    mincostuntilnow = [0 for elem in range(len(cost) + 1)]
    ind = 2
    costOne= 0
    costTwo = 0
    while ind < size+1:
        costOne = mincostuntilnow[ind-1] + cost[ind-1]
        costTwo = mincostuntilnow[ind-2] + cost[ind-2]
        mincostuntilnow[ind] = min(costOne, costTwo)
        ind += 1
    return mincostuntilnow[size]
        
    