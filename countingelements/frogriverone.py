def solution(X, A):
    count = [0] * X

    i = 0
    filled = 0
    while i < len(A) and A[i] <= X:
        position = A[i] - 1
        count[position] += 1
        if count[position] == 1:
            filled += 1
        if filled == X:
            return i
        i += 1

    return -1


print solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
