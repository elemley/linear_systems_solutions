from math import *
import numpy as np


def main():
    #ENGR 3703 Below make up your own examples for each example
    #Please leave the example I have provided and put your example just below

    #this will create a 1-d array (vector)
    x = np.array([0.,1.,2.,3.])
    #print(x)

    #ENGR3703


    #make an array of zeros that is 2 rows by 3 columns
    y = np.zeros((2,3))
    #print(y)

    #ENGR3703


    #make an array that is equally spaced integers from 0-9
    z = np.arange(10)
    #print(z)

    #ENGR3703

    #make an array of floats from 2. to 9.
    yy = np.arange(2,10,dtype=float)
    #print(yy)


    #ENGR3703


    #make an array of floats with spacing other than 1...
    zz = np.arange(2.,3.,0.1)
    #print(zz)

    #ENGR3703

    #make an array with a specified number of points in a range
    yyy = np.linspace(2.,5.,20)
    #print(yyy)

    #ENGR3703

    #make an array that is empty (but you still have space reserved)
    zzz = np.empty([3,2])
    #print(zzz)
    # be careful with this one... you have to fill the matrix yourself.


    #ENGR3703


    #make an array of ones
    yyyy = np.ones((2,3),dtype=float) #note specification of the data type.
    #print(yyyy)

    #ENGR3703

    yyyy = np.ones((2,3))
    #print(yyyy)

    #ENGR3703

    yyyy = np.ones((3,2),dtype=int)
    #print(yyyy)

    #ENGR3703

    #Create a matrix - 'a'
    a_lst = [[0.143, 0.357, 2.01], [-1.31, 0.911, 1.99], [11.2, -4.30, -0.605]]  # this is a list of lists
    a = np.array(a_lst)  # this makes a_lst an 2D array with a maxtrix
    #print(a)

    #ENGR3703

    #Create a matrix - 'b'
    b_lst = [-5.173, -5.458, 4.415]
    # b_lst = [4.0, -2.0,9.0]
    b = np.array(b_lst)  # make the RHS vector
    #print(b)


    #ENGR3703

    #how to augment and get # of rows
    ab = np.c_[a, b]  # we now should have the augmented form - this is just a python numpy library function
    n = len(ab)
    #print(ab)
    #print(n)

    #ENGR3703

    #define matrix 'c'
    c_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists
    c = np.array(c_lst)
    #print(c)


    #ENGR3703


    d_lst = [4.0, -2.0,9.0]
    d = np.array(d_lst)  # make the RHS vector

    #ENGR3703

    #Scalar Product (inner or dot product):
    e = np.dot(b,d)
    #print(e)

    #ENGR3703


    #Matrix Multiply
    f = np.matmul(a,c)
    #print(f)
    #also the @ symbol works
    f=a @ c
    #print(f)

    #ENGR3703

    #what if you use the * symbol...
    #define all the cases so you can see what happens
    g_lst = [[1,2],[3,4]]
    g = np.array(g_lst)
    h = 2.0
    i_lst = [-1, -2]
    i = np.array(i_lst)
    j_lst= [[-1,-2], [-3,-4]]
    j = np.array(j_lst)

    print("g=",g)
    print()
    print("i =",i)
    print()
    print("j=" ,j)
    print()

    print(g*h)
    print()
    print(g*i)
    print()
    print(g*j)
    ## THE BOTTOM LINE IS * does unexpected things... (except when you want to multiply by a scalar

    #If you want to do the same operation on every value in a matrix
    k = a**2    #probably not what you think it is
    print(k)

    #ENGR3703



























if __name__ == '__main__':
    main()
