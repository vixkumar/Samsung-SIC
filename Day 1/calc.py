"""
a = int(input("Enter Number: "))
b = int(input("Enter Number :"))

operation = input("Enter operation to be performed :")
if (operation == "+") :
    print ("Sum = ", a+b)
elif (operation == "-") :
    print ("difference = ", a-b)
elif (operation == "*") :
    print ("Product = ", a*b)
else :
    print ("quoteint :", a/b)
 """

print ("1) Addition\t2) Subtraction\t3) Multiplication\t4)Division ") 
operation = input ("Enter operation")


if operation in (1,2,3,4):
  a = int(input("Enter Number: "))
  b = int(input("Enter Number :"))
  if(operation == "1") :
    print ("Sum = ", a+b)
  elif (operation == "2") :
    print ("difference = ", a-b)
  elif (operation == "3") :
    print ("Product = ", a*b)
  else :
    print ("quoteint :", a/b)
else :
  print ("Invalid syntax")
  