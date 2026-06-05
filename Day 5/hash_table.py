"""
def roman_to_int(str):
    result = 0
    for i in range (len(str)-1):
        if table[str[i]] < table[str[i+1]]:
            result -= table[str[i]]
        else:
            result += table[str[i]]

    return result + table[str[-1]]   

table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roman = input("Input a Roman number: ")
number = roman_to_int(roman)
print(number)    
"""

"""
class Hashtable:
   
    def __init__(self, size):
       self.size = size
       self.table = {}
       for i in range(size):
           self.table[i] = []

    def hash(self, key):
       return key % self.size
   
    def get(self, key):
        return self.table[self.hash(key)]

    def put(self, key, value):
        bucket = self.table[self.hash(key)]
        if value not in bucket:
            bucket.append(value)

Table = Hashtable(8)
book = "Alice in Wonderland"

key = sum(map(ord, book))
print(key, Table.hash(key))

for key in Table.table.keys():

    print(map(ord, Table.table[key])))
"""



            

    

"""
books = ["The little prince", "The old man and sea", "the little mermaid", "Beauty and the beast", "The last leaf"]

for book in books:
    key = sum(map(ord, book))
    print (key, book)
"""

def arabic_to_roman(num):
    table =  [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in table:
        while num >= value:
            result += symbol
            num -= value

    return result

print (arabic_to_roman(900))
