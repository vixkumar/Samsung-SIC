def find_largest(nums):
    largest = 0
    for i in range(1, len(nums)):
        if nums[largest] < nums[i]:
             largest = i
    return largest