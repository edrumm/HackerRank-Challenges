def staircase(n):
    for step in range(1, n + 1):
        line = " " * (n - step)
        line += "#" * step
        print(line)
