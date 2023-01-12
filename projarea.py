#++++++++++++++++++++++++++++++++++
# ProjArea
# Wasam
#++++++++++++++++++++++++++++++++++


def projectionArea(grid):
    def max_len(lol):
        max_ = 0
        for elem in lol:
            if len(elem) > max_:
                max_ = len(elem)
        return max_    
    grid_xz_max = 0
    for elem in grid:
        grid_xz_max += max(elem)    
    grid_xy_num  = 0
    for elem in grid:
        for elem2 in elem:
            if elem2 != 0:
                grid_xy_num += 1
    max_row_len = max_len(grid)
    grid_yz = [[grid[elem][elem2] for elem in range(len(grid))] for elem2 in range(max_row_len)]
    ind2 = 0
    grid_yz_max = 0
    for elem in grid_yz:
        grid_yz_max += max(elem)  
    print(grid_xy_num , grid_xz_max , grid_yz_max)
    return grid_xy_num + grid_xz_max + grid_yz_max

def max_len(lol):
    max_ = 0
    for elem in lol:
        if len(elem) > max_:
            max_ = len(elem)
    return max_
    
    