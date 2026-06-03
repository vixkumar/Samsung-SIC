num = int (input("Enter three digit number: "))
if (num < 100 or num > 999) :
    print ("only three digit number")
elif (num // 100 == 3) :
    print ("True")
else :
    print ("false")

