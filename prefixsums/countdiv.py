def solution(A, B, K):
    left_multiple = int(A / K)
    if A % K != 0:
        if K > A:
            left_multiple = 1
        elif B > K:
            left_multiple = int((A + (K - (A % K))) / K)
        else:
            return 0

    right_multiple = int(B / K)

    if A == B:
        return 0

    return right_multiple - left_multiple + 1


print solution(0, 1, 11)
