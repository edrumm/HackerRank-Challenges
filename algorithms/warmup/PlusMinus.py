def plus_minus(arr):
    if not arr:
        return

    pos, neg, zero = 0, 0, 0
    l = len(arr)

    for num in arr:
        if not num:
            zero += 1
        elif num > 0:
            pos += 1
        else:
            neg += 1

    print(pos / l)
    print(neg / l)
    print(zero / l)
