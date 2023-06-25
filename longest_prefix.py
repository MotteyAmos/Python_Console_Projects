def longest_prefix(arr):
    prefix = ""
    arr.sort()
    first_value = arr[0]
    last_value = arr[len(arr) - 1]
    
    for i in range(len(first_value)):
        if first_value[i] != last_value[i]:
            break
        prefix += first_value[i]
        
    return prefix

