def bin1(n, k):
    if k ==1 or n == k:
        return 1
    else:
        return bin1(n-1, k-1) + bin(n-1, k)
    
n = int(input("Input the value of n : "))
k = int(input("Input the value of k: "))
print(f"binomial{n}, {k} is {bin1(n, k)}")
