def counting_valleys(n, s):
    level, valleys = 0, 0

    for direction in s:
        if direction == "U":
            level += 1
        else:
            level -= 1

        if direction == "U" and level == 0:
            valleys += 1

    return valleys
