def birthday_cake_candles(ar):
    tallest = max(ar)
    out = 0

    for height in ar:
        if height == tallest:
            out += 1

    return out
