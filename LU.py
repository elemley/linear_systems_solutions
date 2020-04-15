from math import *
import numpy as np
import copy
from gauss_fns import *
#a is coefficient matrix (it is rxc) #b is right-hand-side (RHS) (it is cx1) #x is the solution (it is cx1)
def main():
    #Solving system of equations of form:
    # a x = b
    #fns in gauss_fns are:
    # get_sum(ab, x, i) return is summation needed for back_sub
    # back_sub(ab)      return is x -- the solution
    # normalize(ab, i)  return is a new matrix (same size as ab) with row i normalized
    # forward_elim(ab)    return is new matrix (same size as ab) with all forward elim done

    #this is an example from class
    a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
    b_lst = [-5.173, -5.458,4.415]
    a = np.array(a_lst) #this makes the a coefficient maxtrix
    b= np.array(b_lst) #make the RHS vector
    ab = np.c_[a,b]     #augment a with b
    #
    n = len(ab)         #get num of rows
    m = len(ab[0])
    ab_new = copy.deepcopy(ab)
    print(ab_new)
    n = len(ab)         #get num of rows
    m = len(ab[0])
    ab_new = copy.deepcopy(ab)
    #Code below does forward elim. only... to do Gauss-Jordan we need to eliminate above and below diagonal
    for i in range(0,n):      # i is the pivot row... something is not quite right...
        #We are skipping the last row as a pivot row, but now we need to eliminate above the last pivot row...
        ab_new = normalize(ab_new,i)    #we will still need to normalize the pivot row
        for j in range(0,n):          # Now we want to eliminate above and below the pivot
            #now... we need to make sure and not eliminate in the pivot row itself.
            if i!=j:        #ensures we skip the pivot row
                for k in range(i+1,m):  #still OK, we should go from pivot column to end ot augmented matrix
                    ab_new[j,k] -= ab_new[j,i]*ab_new[i,k]      #our basic elimination formula...
                ab_new[j,i] = 0.0
    ab_new = normalize(ab_new,n-1)
    print(ab_new)       #Now the last column contains the x vector!

if __name__ == '__main__':
    main()


#a_lst = [[1.00, 2.50, 14.1], [0.0, 1.0, 4.89], [0.0, 0.0, 1.0]]  # this is a list of lists

#a_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists

# a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
# a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists

# b_lst = [-5.0, -17.0,7.0]
# b_lst = [-5.173, -5.458,4.415]
    #b_lst = [4.0,-2.0,9.0]