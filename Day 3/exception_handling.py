try:
   num = int(input("Enter nume: "))
   denom = int(input("Enter denom: "))
   print(num/denom)

except ZeroDivisionError:
     print("can divide with zero")
else:
    print(num/denom)

finally:
    print("done")
    