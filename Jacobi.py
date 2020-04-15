from math import *
import numpy as np
import copy
def get_sum(a,x,i):
    summ = 0
    n = len(a)
    for j in range(0,n):
        if i!= j:
            summ+=a[i,j]*x[j]
    return summ
def max_rel_err(x_kplus1,x_k):
    max = 0
    for i in range(0,len(x_k)):
        rel_err = abs((x_kplus1[i] - x_k[i]) / x_k[i])
        if rel_err > max:
            max = rel_err
    return max
def main():
    #Solving system of equations of form:
    # a x = b
    #this is an example from class
    a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
    b_lst = [-5.173, -5.458,4.415]
    a = np.array(a_lst) #this makes the a coefficient maxtrix
    b= np.array(b_lst) #make the RHS vector
    n = len(a)
    x_k = np.zeros(n)   #initial guess for x... all zeros will not always be a good guess...
    x_kplus1 = np.zeros(n)
    #x_k = np.array([0.1,0.2,0.33])
    #x_kplus1 = np.array([0.4,0.5,0.6])
    max_iter = 200
    err_stop = 1e-5
    rel_err = 1.1* err_stop
    for count in range(1,max_iter+1):
        for i in range(0,n):
            x_kplus1[i] = (b[i] - get_sum(a,x_k,i))/a[i,i]
        print(x_kplus1)
        if count > 1:
            tmp = max_rel_err(x_kplus1,x_k)
            if tmp < err_stop:
                break
        x_k = copy.deepcopy(x_kplus1)
        print(count)

if __name__ == '__main__':
    main()


#a_lst = [[1.00, 2.50, 14.1], [0.0, 1.0, 4.89], [0.0, 0.0, 1.0]]  # this is a list of lists

#a_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists

# a_lst = [[0.143, 0.357,2.01], [-1.31, 0.911, 1.99],[11.2, -4.30, -0.605]]   #this is a list of lists
# a_lst = [[0.0, 5.0,-1.0], [-4.0, 2.0, 3.0],[4.0, 3.0, 3.0]]   #this is a list of lists

# b_lst = [-5.0, -17.0,7.0]
# b_lst = [-5.173, -5.458,4.415]
    #b_lst = [4.0,-2.0,9.0]