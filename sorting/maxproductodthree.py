def solution(A):
    A.sort()
    print A
    length = len(A)
    right_end = A[length - 1] * A[length - 2] * A[length - 3]
    left_end = A[0] * A[1] * A[length - 1]

    if right_end > left_end:
        return right_end

    return left_end


print solution([-5, 5, -5, 4])
