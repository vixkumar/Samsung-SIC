
def Binary_search(book_ids, target):
   
  
    low, high = 0 , len(book_ids)-1
    comparsions = 0
    while low <=high:
        comparsions += 1
        mid = (low + high) // 2
       
        if book_ids[mid] == target:
            return mid, comparsions
            

        elif target > book_ids[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparsions

book_ids = [1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040]
target = int(input("Enter Book ID: "))

position, comparsions = Binary_search(book_ids, target)

if position != -1:
    print ("Book Found")
    print("Position: ", position)
    print ("Comparisons: ",comparsions)

if position == -1:
    print ("Book not Found")
    print ("Comparisons: ",comparsions)





    

        

        

    
