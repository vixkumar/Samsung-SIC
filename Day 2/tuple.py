"""
student_tup = (('211101', 'David Doe', '010-1234-4500'),
               ('211102', 'John Smith', '010-2230-6540'),
               ('211103', 'Jane Carter', '010-3232-7788'))
result = {i[0] : i[1:] for i in student_tup}
print(result)
Conversion from tuple to dict
"""


student_tup =(('211101', 'David Doe', '010-1234-4500'),
               ('211102', 'John Smith', '010-2230-6540'),
               ('211103', 'Jane Carter', '010-3232-7788'))
iname = input("Enter input: ")
for id, name, number in student_tup:
    if iname == name:
       print("student ID number: ", id)
       print ("Name :", name)
       print("Phone Number :", number)

       break

else:
    print("error")


  



