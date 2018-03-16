def solution(N, A):
    counters = [0] * N

    i = 0
    max_counter = 0
    while i < len(A):
        print A[i]
        if A[i] == N + 1:
            if max_operation_last:
                max_counter += 1
            else:
                position = A[i - 1] - 1
                if N > position >= 0:
                    max_counter = counters[position]
            max_operation_last = True
        elif 1 <= A[i] <= N:
            if max_operation_last:
                counters[A[i] - 1] = max_counter + 1
            else:
                counters[A[i] - 1] += 1
            max_operation_last = False
        i += 1
        print counters

    j = 0
    while j < N:
        if counters[j] < max_counter:
            counters[j] = max_counter
        j += 1

    return counters


print solution(5, [1, 6, 2, 6, 1])
