def get_total_x(a, b):
    return sum([
        all(i % x == 0 for x in a) and
        all(x % i == 0 for x in b) for i in range(1, 101)])
