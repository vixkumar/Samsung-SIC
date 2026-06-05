"""
#Binary Search
def bin_search(nums, x):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid]>x:
            high = mid - 1
        else:
            low = mid + 1
    return - 1

nums = list(map(int, input("Enter nums: ").split()))
x = int(input("Target to be searched: "))
target = bin_search(nums,x)
print ("Target found at index number: ", target)
"""


"""
from random import randint

def do_experiment(floor,breaking):
    return floor >= breaking
def find_highest_safe_floor(height, breaking):
    for n in range (1, height + 1):
        if  do_experiment(n, breaking):
            return n-1

height = int(input("Input the number of floors: "))
breaking = randint(1, height)
breaking = int(input("Input the first breaking floor: "))
floor = find_highest_safe_floor(height, breaking)
print(f"Your egg will be safe till the {floor} --th floor.")
"""

"""
def do_experiment(floor, breaking):
    return floor >= breaking

def find_safe_highest_floor2(height, breaking):
    low, high = 1, height
    while low < high:
        mid = (low + high) //2
        if do_experiment(mid, breaking):
         high = mid
        else:
          low = mid + 1
    return low - 1

height = int(input("Enter height or total floors of building: "))
breaking = int(input("Enter flor where egg broke: "))
floor = find_safe_highest_floor2(height, breaking)
print("Highest safe floor is : ", floor)
"""

maximum = int(input("Enter maximum or range: "))
number = int(input("Enter number to be searched: "))

low, high = 1, maximum
count = 0

while low<=high:
    mid = (low + high) // 2
    count+= 1
    if mid == number:
        print(f"Your number is :{number}")
        break
    elif mid > number:
        high = mid -1
    else:
        low = mid + 1

print(f"Total {count} times are searched")








