def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_landed, oranges_landed = 0, 0

    for i in range(len(apples)):
        if (a + apples[i]) in range(s, t + 1):
            apples_landed += 1

    for i in range(len(oranges)):
        if (b + oranges[i]) in range(s, t + 1):
            oranges_landed += 1

    print(apples_landed)
    print(oranges_landed)
