"""
data = {"Last Name" : "Doe", 
        "First Name" : "David", 
        "Company" : "Samsung"}
for key, value in data.items():
    print(f"{key}: {value}")
    """

items = {"coffee" : 7, "Pen" : 3, "paper cup" : 2, "Milk" : 1, "Coke" : 4, "Book" : 5}
item = input("Enter item: ")

inventory = items.get(item)
if item in items:
    print(inventory)
else:
    print("not present")
    






    

        

