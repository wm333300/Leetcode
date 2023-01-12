#=============================
# Maximum Profit
# By Wasam
#=============================



def maxProfit(prices):
    ind = 0
    profit = 0
    curr_num = 0
    profit_list = []
    while ind < len(prices)-1:
        curr_num = prices[ind]
        inner_list = []
        for elem in prices[ind+1:]:
            profit =  elem - curr_num
            inner_list.append(profit)
        profit_list.append(max(inner_list))
        ind += 1
    return max(profit_list)