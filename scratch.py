n = len(ab)  # get num of rows
ab_new = copy.deepcopy(ab)
for i in range(0, n - 1):
    ab_new = normalize(ab_new, i)
    for j in range(i + 1, n):
        for k in range(i + 1, m):
            ab_new[j, k] -= ab_new[j, i] * ab_new[i, k]
        ab_new[j, i] = 0.0
ab_new = normalize(ab_new, n - 1)

for i in range(0, n):  # i=pivot row... Start at 0 and go to next to last row
    ab_new = normalize(ab_new, i)  # normalize before pivoting
    for j in range(0, n):  # eliminate above and below the pivot
        if i != j:  # skip the pivot row
            for k in range(i + 1, m):
                ab_new[j, k] -= ab_new[j, i] * ab_new[i, k]
            ab_new[j, i] = 0.0

ab_new = normalize(ab_new, n - 1)

# this is an example from class
a_lst = [[0.143, 0.357, 2.01], [-1.31, 0.911, 1.99], [11.2, -4.30, -0.605]]  # this is a list of lists
# a_lst = [[1.0, -3.0, 1.0],[2.0, -8.0, 8.0],[-6.0, 3.0,-15.0]]   #this is a list of lists
b_lst = [-5.173, -5.458, 4.415]
# b_lst = [4.0,-2.0,9.0]
# a = np.array(a_lst) #this makes the a coefficient maxtrix
# b= np.array(b_lst) #make the RHS vector
