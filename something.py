import numpy as np
"""
Playing with numpy...
Olivier 6 sep 2022
"""
SIZE=10

def fillMatrix(m):
    for i in range(0,10):
        for j in range(0,10):
            m[i][j]=8
    return

def printMatrix(m):
    for i in range(0,10):
        for j in range(0,10):
            print(m[i][j],end=" ")
        print(" ")
    return

def main():
    #making a matrix filled with zeros, specifying the shape (10,10) and the datatype dtype=int
    matrix = np.zeros((10,10),dtype=int)
    fillMatrix(matrix) #filling the matrix with a chosen value
    printMatrix(matrix) #printing the matrix to the terminal



#calling the main function
main()