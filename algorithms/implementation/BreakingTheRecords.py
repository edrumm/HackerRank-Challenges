def breaking_records(score):
    highest = score[0]
    lowest = score[0]
    h_count, l_count = 0, 0

    for s in score:
        if s > highest:
            highest = s
            h_count += 1
        elif s < lowest:
            lowest = s
            l_count += 1

    return [h_count, l_count]
