"""
def coin_change(coins, amount):
    coins.sort(reverse=True)
    changes = []
    largest = 0
    while amount > 0:
        if amount < coins[largest]:
            largest +=1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]
    return changes


coins1 = [10, 20, 50, 100, 200, 500]
amount1 = 870

print(coin_change(coins1, amount1))
"""

def coin_change(coins, amount):
    coins.sort(reverse=True)
    changes = []
    largest = 0
    while amount > 0:
        if amount < coins[largest]:
            largest +=1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]
    return changes
    print(changes.len())
    

coins1 = list(map(int, input("Enter coins: ").split()))
amount1 = int(input("Enter Amount: "))

print(coin_change(coins1, amount1))

