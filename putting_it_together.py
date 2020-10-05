from math import *
import numpy as np
import copy
from gauss_fns import *
# fns in gauss_fns are:
# get_sum(ab, x, i) return is summation needed for back_sub
# back_sub(ab)      return is x -- the solution
# normalize(ab, i)  return is a new matrix (same size as ab) with row i normalized
# forward_elim(ab)    return is new matrix (same size as ab) with all forward elim done
# ...and more

#a is coefficient matrix (it is rxc) #b is right-hand-side (RHS) (it is cx1) #x is the solution (it is cx1)

def main():
    #Solving system of equations of form:
    # a x = b
    #this is an example from class
    a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
    b_lst = [-5.173, -5.458,4.415]
    #a = np.array(a_lst) #this makes the a coefficient maxtrix
    #b= np.array(b_lst) #make the RHS vector
    a = np.array([[9., 2., 3., 2.], [2., 8., -2., 3.], [-3., 2., 11.,-4.], [-2., 3., 2., 10.]])
    b = np.array([[54.5], [-14], [12.5],[-21] ])
    ab = np.c_[a,b]     #augment a with b
    ab_new, x, order = partial_pivot_gauss(ab)
    print_ordered(ab_new,order)
    print_ordered(x,order)



if __name__ == '__main__':
    main()


#a_lst = [[1.00, 2.50, 14.1], [0.0, 1.0, 4.89], [0.0, 0.0, 1.0]]  # this is a list of lists

#a_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists

# a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
# a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists

# b_lst = [-5.0, -17.0,7.0]
# b_lst = [-5.173, -5.458,4.415]
    #b_lst = [4.0,-2.0,9.0]