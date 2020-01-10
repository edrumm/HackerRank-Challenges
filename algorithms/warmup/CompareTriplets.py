def compare_triplets(a, b):
    ascore = sum([(1 if a[i] > b[i] else 0) for i in range(len(a))])
    bscore = sum([(1 if b[i] > a[i] else 0) for i in range(len(b))])
    return [ascore, bscore]
