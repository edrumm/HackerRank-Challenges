def designer_pdf_viewer(h, word):
    tallest = 0

    for i in range(len(word)):
        j = ord(word[i]) - 97
        if h[j] > tallest:
            tallest = h[j]

    return tallest * len(word)
