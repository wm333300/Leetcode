# Rot Img

v1 = [[1,2,3],[4,5,6],[7,8,9]]
v2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate_(matrix):
    breaker = False
    for elem in range(len(matrix)):
        for e2 in range(len(matrix)):
            if ((elem == ((len(matrix)-1)//2)) and (e2 == ((len(matrix)-1)//2))):
                breaker = True
                break 
            else:
                intermediate = matrix[elem][e2]
                matrix[elem][e2] = matrix[len(matrix)-1-elem][len(matrix)-1-e2]
                matrix[len(matrix)-1-elem][len(matrix)-1-e2] = intermediate 
                #print(matrix, elem, e2)            
        if breaker:
            break
    return matrix

def mat_T(m):
    for e1 in range(len(m)):
        interm = 0
        for e2 in range(len(m)):
            if e2 >= e1:
                interm = m[e2][e1]
                m[e2][e1] = m[e1][e2]
                m[e1][e2] = interm
def rotate(m):
    m.reverse()
    mat_T(m)
