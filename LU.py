from math import *
import copy
import numpy as np
import scipy
import scipy.linalg

def get_sum(L,U,i,j):
    summ = 0
    for k in range(0,j):
        summ+=L[i][k]*U[k][j]
    return summ

def LU_Crout(a):
    n = len(a)
    L = np.zeros((n,n),dtype=float)
    U = np.zeros((n, n), dtype=float)
    #Fill in first column (all the L's are just equal to the a's)
    for i in range(0,n):
        L[i][0]=a[i][0]
    print(f"L = \n {L}")
    #fill in the diagonal of the U with 1's
    for i in range(0,n):
        U[i][i] = 1.0
    print(f"U = \n {U}")
    #Fill in the first row of U with simple formula
    for j in range(1,n):
        U[0][j] = a[0][j]/L[0][0]
    print(f"U = \n {U}")
    #Now fill in the rest of both U and L
    for i in range(1,n):
        #Work from the second row to the bottom
        for j in range(1,n):
            #Work from second column to last
            if j<= i :
                #To the left and on the diagonal calc. L values
                L[i][j]=a[i][j] - get_sum(L,U,i,j)
            else:
                #To the right of the diagonal calc. U values
                U[i][j] = (a[i][j] - get_sum(L, U, i, j)) / L[i][i]
    return L,U

def main():
    A = np.array([[4.,-2.,-3.,6.],[-6.,7.,6.5,-6.],[1.,7.5,6.25,5.5],[-12.,22.,15.5,-1.]])
    B = np.array([[14],[-1],[14]])

    L,U = LU_Crout(A)
    print(f"The solution for L = \n {L}")
    print(f"The solution for U = \n {U}")
    print(f"LU = {np.matmul(L,U)}")
    print(f"A = {A}")



    #P,L,U = scipy.linalg.lu(A)
    #print(f"P={P} \n L={L} \n U={U}")




if __name__ == '__main__':
    main()
