def max_sub_array(arr):
    max_sum = float('-inf')
    for i in range (len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
    return max_sum = max(max_sum, total)
    
 max_sum = [-2, -1, ]