from math import *
import numpy as np

#a is coefficient matrix (it is rxc)
#b is right-hand-side (RHS) (it is cx1)
#x is the solution (it is cx1)

def augment(a,b):
    #set things up for Gaussian elim.
    ab = np.c_[a, b]  # we now should have the augmented form - this is just a python numpy library function
    return ab

def get_sum(ab,x,order,i):
    #stuff
    return 1


def main():

    #this is an example from class
    #a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
    #a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists

    a_lst = [[-4, 2, 3],[0, 5, -1],[4, 3,3]]   #this is a list of lists
    a = np.array(a_lst) #this makes a_lst an 2D array


    #b_lst = [-5.173, -5.458,4.415]
    #b_lst = [-5.0, -17.0,7.0]
    b_lst = [-17, -5,7]
    b= np.array(b_lst)

    #print a,b
    #a = np.empty(shape=(n,n))
    #b = np.empty(shape=(n,1))

    ab = augment(a,b)   #augment the b RHS vector on the right side of a
    n = len(ab)         #number of rows in ab
    print(ab)

    print(ab[0,0])
    print(ab[1,1])
    print(ab[0])
    print(ab[1])
    print(ab[2])

if __name__ == '__main__':
    main()





