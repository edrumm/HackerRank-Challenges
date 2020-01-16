def diagonal_difference(arr):
    primary = 0
    secondary = 0

    for i in range(len(arr)):
        j = len(arr[0]) - i - 1
        primary += arr[i][i]
        secondary += arr[i][j]

    return abs(primary - secondary)


print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
