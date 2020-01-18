def mini_max_sum(arr):
    max_sum = 0
    min_sum = sum(arr) - arr[0]

    for i in range(len(arr)):
        max_sum = max((sum(arr) - arr[i]), max_sum)
        min_sum = min((sum(arr) - arr[i]), min_sum)

    print(min_sum, max_sum)
