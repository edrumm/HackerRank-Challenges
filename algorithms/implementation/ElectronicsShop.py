def get_money_spend(keyboards, drives, b):
    highest = min(keyboards) + min(drives)

    if highest > b:
        return -1

    for kprice in keyboards:
        for dprice in drives:
            total = kprice + dprice

            if total > highest and total <= b:
                highest = total

    return highest
