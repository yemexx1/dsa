def solution(A):
    length = len(A)
    count = [0] * length

    i = 0
    while i < length:
        position = A[i] - 1
        if position > length - 1:
            return 0

        count[position] += 1

        if count[position] > 1:
            return 0

        i += 1

    return 1


print solution([1, 1, 1])
