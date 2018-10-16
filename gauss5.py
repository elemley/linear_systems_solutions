from math import *
import numpy as np
import copy

#a is coefficient matrix (it is rxc)
#b is right-hand-side (RHS) (it is cx1)
#x is the solution (it is cx1)

def get_ordered(a,order):
    ab_new = copy.deepcopy(a)
    n = len(a)
    for i in range(0,n):
        for j in range(0,n+1):
            ab_new[i,j] = a[order[i],j]
    return ab_new

def augment(a,b):
    #set things up for Gaussian elim.
    ab = np.c_[a, b]  # we now should have the augmented form - this is just a python numpy library function
    return ab

def get_sum(ab,x,i):
    summ = 0
    n = len(ab)     #gets # of rows in augmented matrix
    for j in range(i+1,n):
        summ+=ab[i,j]*x[j]      #gets the summation we need for each xi in back sub
    return summ

def back_sub(ab):
    n = len(ab)
    x = np.empty((n,1))         #make an empty matrix with n rows and 1 column
    x[n - 1] = ab[n-1,n] / ab[n - 1, n - 1]     #Find x_n-1 value of x for last row
    for i in range(n - 2, -1, -1):             #Now work through remaining rows - start at n-2 and go backwards to row 0
        summ = get_sum(ab, x, i)                #use get_sub to return value of summation
        x[i] = (ab[i,n] - summ) / ab[i][i]      #this is the back sub equation we derived from class
    return x

def normalize(ab,i):
    n = len(ab)
    new_ab = copy.deepcopy(ab)
    norm = ab[i,i]
    for j in range(i,n+1):
        new_ab[i,j] = ab[i,j] / norm
    return new_ab

def forward_sub(ab_orig,i):
    n = len(ab_orig)
    ab_orig = normalize(ab_orig,i)
    ab = copy.deepcopy(ab_orig)
    for k in range(i+1,n):
        for j in range(i,n+1):
            ab[k,j]-= ab_orig[k,i]*ab_orig[i,j]
    return ab

def main():
    #Solving system of equations of form:
    # a x = b
    #this is an example from class
    a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
    #a_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists
    a = np.array(a_lst) #this makes a_lst an 2D array with a maxtrix

    b_lst = [-5.173, -5.458,4.415]
    #b_lst = [4.0, -2.0,9.0]
    b= np.array(b_lst) #make the RHS vector

    ab = augment(a,b)   #augment the b RHS vector on the right side of a
    n = len(ab)

    #order = [1,0,2]
    #ab_ordered = ab[:]
    #ab_ordered=get_ordered(ab,order)
    #print(ab_ordered)

    ab_old = copy.deepcopy(ab)
    ab_new = copy.deepcopy(ab)

    for i in range(0,n-1):
        ab_new = forward_sub(ab_old,i)
        ab_old = copy.deepcopy(ab_new)

    ab_final = normalize(ab_new,n-1)
    print(ab_final)

    x = back_sub(ab_final)
    print(x)


if __name__ == '__main__':
    main()





# a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
# a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists
# b_lst = [-5.173, -5.458,4.415]
# b_lst = [-5.0, -17.0,7.0]
