def bon_appetit(bill, k, b):
    total = (sum(bill) - bill[k]) // 2
    if total != b:
        cost_diff = (b - total)
        print(cost_diff)
    else:
        print("Bon Appetit")
