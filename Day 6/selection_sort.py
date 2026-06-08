def selection_sort(S):
    n = len(S)
    for i in range(n-1):
        print(S)
        smallest = i
        for j in range(i+1, n):
            if S[j] < S[smallest]:
                smallest = j 
        S[i], S[smallest] = S[smallest], S[i]

S = [10, 30,  20 , 50, 40]
selection_sort(S)
print(S)
