# GREEDY ALGORITHM
# best choice as it is fast but only optimal for special problem

def make_change(amount):
    coins = [500, 200, 50, 20, 10, 5 ,2 ,1]
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    return result
change = make_change(87)
print("coins used:", change)
print("total coins:", len(change))