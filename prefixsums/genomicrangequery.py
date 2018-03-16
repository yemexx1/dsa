def solution(S, P, Q):
    n = len(S)

    a_prefix_sums = [0] * (n + 1)
    c_prefix_sums = [0] * (n + 1)
    g_prefix_sums = [0] * (n + 1)
    t_prefix_sums = [0] * (n + 1)

    for i in range(1, n + 1):
        character = S[i - 1]

        a_prefix_sums[i] = a_prefix_sums[i - 1]
        c_prefix_sums[i] = c_prefix_sums[i - 1]
        g_prefix_sums[i] = g_prefix_sums[i - 1]
        t_prefix_sums[i] = t_prefix_sums[i - 1]

        if character == 'A':
            a_prefix_sums[i] += 1
        elif character == 'C':
            c_prefix_sums[i] += 1
        elif character == 'G':
            g_prefix_sums[i] += 1
        else:
            # T
            t_prefix_sums[i] += 1

    m = len(P)
    results = [0] * m
    for j in range(m):
        if a_prefix_sums[Q[j] + 1] - a_prefix_sums[P[j]] > 0:
            results[j] = 1
        elif c_prefix_sums[Q[j] + 1] - c_prefix_sums[P[j]] > 0:
            results[j] = 2
        elif g_prefix_sums[Q[j] + 1] - g_prefix_sums[P[j]] > 0:
            results[j] = 3
        else:
            results[j] = 4
    return results


print solution("CAGCCTA", [2, 5, 0], [4, 5, 6])
