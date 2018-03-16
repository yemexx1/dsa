def prefixsum(A):
    n = len(A)
    prefixsums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsums[i] = prefixsums[i - 1] + A[i - 1]

    return prefixsums


def solution(A):
    P = prefixsum(A)
    Pn = len(P)

    i = Pn - 1
    num_zeros = 0
    pairs = 0
    while i > 0:
        if P[i] - P[i - 1] == 0:
            pairs += Pn - i - 1 - num_zeros
            num_zeros += 1

        if pairs > 1000000000:
            pairs = -1
            break

        i -= 1

    return pairs


print solution([0, 1, 0, 1, 1])
