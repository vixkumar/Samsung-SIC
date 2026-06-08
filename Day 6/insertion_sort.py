def insertion_sort1(S):
    n = len(S)
    R = []
    while len(S) > 0:
        print(R, S)
        x = S.pop(0)
        j = len(R) - 1
        while j >=0 and R[j] > x:
            j-= 1
            R.insert(j+1, x)
        return R

S = [50, 30, 40, 10, 20]
R = insertion_sort1(S)
print(R)
