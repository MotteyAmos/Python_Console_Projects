def binarySearch(data_list, value):
    lower = 0
    upper = len(data_list) - 1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        
        if data_list[mid] == value:
            return (value, mid)
        elif data_list[mid] < value:
            lower = mid + 1
        elif data_list[mid] > value:
            upper = mid -1
    
    if lower > upper:
        return None

data_list = [x for x in range(10)]
result = binarySearch(data_list, 5)

print(data_list)
print(result)



