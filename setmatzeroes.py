# Set Matrix Zeroes

v1 = [[1,1,1],[1,0,1],[1,1,1]]
v2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def setZeroes(matrix):
    zeroRows = []
    zeroCols = []
    for elem in range(len(matrix)):
        if (0 in matrix[elem]):
            for elem2 in range(len(matrix[0])):
                if (matrix[elem][elem2] == 0):
                    zeroRows.append(elem)
                    zeroCols.append(elem2)
    for elem in range(len(matrix)):
        for elem2 in range(len(matrix[0])):
            if ((elem in zeroRows) or (elem2 in zeroCols)):
                matrix[elem][elem2] = 0
    return matrix