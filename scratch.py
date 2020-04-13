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
