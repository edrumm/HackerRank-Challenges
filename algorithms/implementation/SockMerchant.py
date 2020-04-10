from collections import Counter

def sock_merchant(n, ar):
    counts = Counter(ar)
    pairs = 0

    for colour, occ in counts.items():
        if occ > 1 and occ % 2 == 0:
            pairs += occ // 2
        elif occ > 1 and (occ - 1) % 2 == 0:
            pairs += occ // 2

    return pairs


sock_merchant(7, [1, 2, 1, 2, 1, 3, 2])
