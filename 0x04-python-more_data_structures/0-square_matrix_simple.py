#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != []:
        newmatrix = [i[:] for i in matrix]
        for row in range(len(newmatrix)):
            for col in range(len(newmatrix[row])):
                    newmatrix[row][col] = newmatrix[row][col]**2
        return (newmatrix)
