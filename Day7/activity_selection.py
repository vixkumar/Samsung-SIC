def activity_selection (start, finish):
    result = []
    i = 0
    result.append(i)
    for j in range(1, len(start)):
        if(finish[i] <= start[j]):
            result.append(j)
            i=j
    return result

start = [1, 2, 3, 4 ,5]
end=[4, 5, 6, 7, 8]
meetings = activity_selection(start, end)
print(meetings)

