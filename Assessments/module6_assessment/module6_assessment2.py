grid = [
    [1, 3, 5],
    [2, 1, 2],
    [4, 3, 1]
]

n = len(grid)
m = len(grid[0])

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + grid[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print("Dynamic Programming Table")
for row in dp:
    print(*row)

print("\nMinimum Transportation Cost =", dp[n-1][m-1])

path = []
i, j = n - 1, m - 1

while i > 0 or j > 0:
    path.append((i, j))

    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif dp[i-1][j] < dp[i][j-1]:
        i -= 1
    else:
        j -= 1

path.append((0, 0))
path.reverse()

print("\nOptimal Route:")
print(" -> ".join(str(p) for p in path))