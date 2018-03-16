def prefixsum(A):
    n = len(A)
    prefixsums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsums[i] = prefixsums[i - 1] + A[i - 1]

    return prefixsums


def solution(A):
    P = prefixsum(A)
    Pn = len(P)

    print A
    print P

    start_position = len(A)
    minimum = 20000
    for i in range(2, Pn):
        for j in range(i, Pn):
            avg = (P[j] - P[j - i]) / i
            slice_start = j - i
            if avg < minimum:
                if avg == minimum:
                    if slice_start < start_position:
                        start_position = slice_start
                else:
                    start_position = slice_start
                minimum = avg

    return start_position


def solution_with_difference(A):
    P = prefixsum(A)
    print P




print solution_with_difference([4, 2, 2, 5, 1, 5, 8])
