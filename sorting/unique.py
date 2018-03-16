def solution(A):
    A.sort()

    if len(A) == 0:
        return 0

    i = 1
    result = 1
    while i < len(A):
        if A[i] != A[i - 1]:
            result += 1
        i += 1
    return result


solution([2, 2, 1, 3, 1, 1])
