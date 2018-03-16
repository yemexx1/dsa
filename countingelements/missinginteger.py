def solution(A):
    maximum = max(A)
    if maximum < 0:
        return 1

    zero_value = maximum * 2
    count = [0] * zero_value

    i = 0
    zero_position = int(len(count) / 2)
    while i < len(A):
        position = zero_value - (A[i] + zero_value)
        if position > 0:
            count[zero_position - position] += 1
        elif position < 0:
            count[abs(position + 1) + zero_position] += 1
        i += 1

    j = zero_position
    while j < len(count):
        if count[j] == 0:
            return j - zero_position + 1
        j += 1

    return j - zero_position + 1

print solution([-1, -3])