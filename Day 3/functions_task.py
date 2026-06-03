def mean3(a,b,c):
    mean =( a + b + c ) / 3
    print("mean of three numbers is: ", mean)

def max(a,b,c):
    if(a>b and a>c):
        max = a
    elif(b>a and b>c):
        max = b
    else:
        max = c
    print("max of three numbers is: ", max)


d,e,f = map(int, input("Enter three numbers: ").split()) # refer how inputs are taken
mean3(d,e,f)
max(d,e,f)



