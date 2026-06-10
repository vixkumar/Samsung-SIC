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


coins1 = [500, 200, 100, 50, 20]
amount1 = int(input("Withdrawal Amount: "))
notes = coin_change(coins1, amount1)

print("Denomination Breakdown:")
total_notes = len(notes)

for i in coins1:
    count = notes.count(i)
    if count > 0:
        print(f"₹{i} × {count} = ₹{i * count}")

print(f"\nTotal Notes Dispensed = {total_notes}")


