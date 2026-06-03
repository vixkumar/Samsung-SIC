f = open('data5.txt', 'w')
for _ in range (5):
    n = input ("Enter Intger: ")
    f.write(n)
    f.write('\n')
f.close()

