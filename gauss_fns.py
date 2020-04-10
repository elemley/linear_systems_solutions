from math import *
import numpy as np
import copy
#a is coefficient matrix (it is rxc) #b is right-hand-side (RHS) (it is cx1) #x is the solution (it is cx1)
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
def forward_elim(ab):
    n = len(ab)         #get num of rows
    ab_new = copy.deepcopy(ab)
    for i in range(0,n-1):
        ab_new = normalize(ab_new,i)
        for j in range(i+1,n):
            for k in range(i+1,m):
                ab_new[j,k] -= ab_new[j,i]*ab_new[i,k]
            ab_new[j,i] = 0.0
    ab_new = normalize(ab_new,n-1)
    return ab_new
def pivot(ab,i,order):          #Find best row for current pivot row
    n = len(ab)
    max = abs(ab[i,i])
    index = i
    for j in range(i+1,n):
        if abs(ab[j,i]) > max:
            index = j
            max = abs(ab[j,i])
    tmp = order[i]
    order[i] = order[index]
    order[index] = tmp
    return order
def print_ordered(ab,order):
    ab_new = copy.deepcopy(ab)
    n = len(ab)
    m = len(ab[0])
    for i in range(0,n):
        for j in range(0,m):
            ab_new[i,j] = ab[order[i],j]
    print(ab_new)
def normalize_pp(ab,i,order):
    n = len(ab)
    new_ab = copy.deepcopy(ab)
    norm = ab[order[i],i]
    for j in range(i,n+1):
        new_ab[order[i],j] = ab[order[i],j] / norm
    return new_ab
def get_sum_pp(ab,x,i,order):
    summ = 0
    n = len(ab)     #gets # of rows in augmented matrix
    for j in range(i+1,n):
        summ+=ab[order[i],j]*x[order[j]]      #gets the summation we need for each xi in back sub
    return summ
def back_sub_pp(ab,order):
    n = len(ab)
    x = np.empty((n,1))         #make an empty matrix with n rows and 1 column
    x[order[n - 1]] = ab[order[n-1],n] / ab[order[n - 1], n - 1]     #Find x_n-1 value of x for last row
    for i in range(n - 2, -1, -1):             #Now work through remaining rows - start at n-2 and go backwards to row 0
        summ = get_sum_pp(ab, x, i,order)                #use get_sub to return value of summation
        x[order[i]] = (ab[order[i],n] - summ) / ab[order[i]][i]      #this is the back sub equation we derived from class
    return x
def partial_pivot_gauss(ab):
    n = len(ab)
    m = len(ab[0])
    order = np.arange(n)
    ab_new = copy.deepcopy(ab)
    for i in range(0,n-1):
        order = pivot(ab_new, i, order)  # Do complete elimination and normalize entire diagonal (use partial pivoting)
        ab_new = normalize_pp(ab_new,i,order)
        for j in range(i+1,n):
            for k in range(i+1,m):
                ab_new[order[j],k] -= ab_new[order[j],i]*ab_new[order[i],k]
            ab_new[order[j],i] = 0.0
    ab_new = normalize_pp(ab_new,n-1,order)
    x = back_sub_pp(ab_new,order)
    return ab_new, x, order











