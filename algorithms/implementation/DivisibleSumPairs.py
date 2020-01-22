def divisible_sum_pairs(n, k, ar):
    divisible = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                divisible += 1

    return divisible
