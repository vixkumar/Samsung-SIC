def bin3(n, k):
    B = [0] * (n + 1)
    for i in range(n, -1, -1):
        for j in range (n,-1, -1):
            if j ==0 or j ==i:
                 B[j] = 1
            else:
                B[j] = B[j] + B[j -1]
    return B[k]

for i in range(10):
    for j in range(i*1):
        print(bin3(i,j), end= " ")
    print()

def fib4(n):
    if n<=1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b

N = int(input("Input a number: "))
print(fib4(N))