def birthday(s, d, m):
    start, splits, end = 0, 0, m
    sub = []

    while end <= len(s):
        sub = s[start:end]

        if sum(sub) == d:
            splits += 1

        start += 1
        end = start + m

    return splits if splits else 0
