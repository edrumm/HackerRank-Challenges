def utopian_tree(n):
    height = 1

    for cycle in range(1, n + 1):
        if cycle % 2 == 0:
            height += 1
        else:
            height *= 2

    return height
