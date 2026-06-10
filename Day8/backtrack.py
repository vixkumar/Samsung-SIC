def n_queens(i, col):
    if promising(i, col):
        if i == len(col) - 1:
            print(col)
    else:
        for j in range(len(col)):
            col[i + 1] = j
        
        n_queens(i + 1, col)

def promising(i, col):
    for k in range(i):
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
    return True