def migratory_birds(arr):
    common = 0
    for t in range(2, 6):
        if arr.count(t) > arr.count(t - 1):
            common = t

    return common

# Alternate solution:
#
# from collections import Counter
# count = Counter(arr).most_common(1)
# return count[0][0]
