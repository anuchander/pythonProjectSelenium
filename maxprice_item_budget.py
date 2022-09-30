
def max_price_item(keyboard, drives, budget):
    k_len = len(keyboard)
    d_len = len(drives)
    max_total=0
    for i in keyboard:
        for j in drives:
            total = i+j
            if (total>max_total and total<=budget):
                max_total= total
    return max_total




keyboard = [5, 2, 8]
drives =  [3,1]
b = 9
max_budget_item = max_price_item(keyboard, drives, b)
print(max_budget_item)
