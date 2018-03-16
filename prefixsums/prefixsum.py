def prefixsum(A):
    n = len(A)
    prefixsums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsums[i] = prefixsums[i - 1] + A[i - 1]

    return prefixsums


def count_total(P, x, y):
    return P[y + 1] - P[x]


P = prefixsum([0, 1, 0, 1, 1])
print P

#print count_total(P, 0, 0)

