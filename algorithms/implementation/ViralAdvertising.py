def viral_advertising(n):
    recieved = 2
    likes = recieved

    for day in range(n - 1):
        recieved = int(3 * recieved / 2)
        likes += recieved

    return likes
