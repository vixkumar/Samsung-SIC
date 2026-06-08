def heavy_coin(coins, weight):
    if len(coins) == 1:
        return coins[0]
    mid = len(coins) //2

    left_coins = coins[:mid]
    right_coins = coins[mid:]

    left_weight = weight[:mid]
    right_weight = weight[mid:]
    count = 0

    if sum(left_weight) > sum(right_weight):
        return heavy_coin(left_coins, left_weight)
    else:
        return heavy_coin(right_coins, right_weight)
        

    
coins = [1, 2, 3, 4, 5, 6, 7, 8]
weight = [0, 0, 0, 1, 0, 2, 0, 1]

print(heavy_coin(coins, weight))