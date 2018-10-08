from math import *
import numpy as np

#a is coefficient matrix (it is rxc)
#b is right-hand-side (RHS) (it is cx1)
#x is the solution (it is cx1)

def augment(a,b):
    #set things up for Gaussian elim.
    ab = np.c_[a, b]  # we now should have the augmented form - this is just a python numpy library function
    return ab

def get_sum(ab,x,i):
    summ = 0
    n = len(ab)
    for j in range(i+1,n):
        summ+=ab[i,j]*x[j]
    return 1

def main():
    #this is an example from class
    a_lst = [[1, -3, 1],[0, 1, -3],[0, 0,1]]   #this is a list of lists
    a = np.array(a_lst) #this makes a_lst an 2D array
    b_lst = [4, 5,-2]
    b= np.array(b_lst)
    n = len(ab)         #number of rows in ab
    x[n-1] = b[n-1]/a[n-1,n-1]
    for i in range(n-2,-1,-1):




    #print a,b
    #a = np.empty(shape=(n,n))
    #b = np.empty(shape=(n,1))

    ab = augment(a,b)   #augment the b RHS vector on the right side of a

    print(ab)

    print(ab[0,0])
    print(ab[1,1])
    print(ab[0])
    print(ab[1])
    print(ab[2])

if __name__ == '__main__':
    main()





# a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
# a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists
# b_lst = [-5.173, -5.458,4.415]
# b_lst = [-5.0, -17.0,7.0]
