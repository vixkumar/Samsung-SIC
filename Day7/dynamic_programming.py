F = {0:0, 1:1}

def fib2(n):
    if n in F:
        return F[n]
    else:
        F[n] = fib2(n-1) + fib2(n-2)
        return F[n]
    
N = int(input("Input a number: "))
print(fib2(N))
