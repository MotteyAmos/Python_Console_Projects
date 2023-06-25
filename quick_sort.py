import random

def pivort(data_list, first, last):
    pivort = data_list[first]
    left = first + 1
    right = last
    
    while True:
        while left <= right and data_list[left] <= pivort:
            left += 1
        while left <= right and data_list[right] >= pivort:
            right -= 1
        
        if right < left:
            break
        else:
            data_list[left], data_list[right] = data_list[right], data_list[left]
    
    data_list[first], data_list[right] = data_list[right], data_list[first]
    
    return right


def quick_sort(data_list, first, last):
    
    if first < last:
        p = pivort(data_list, first, last)
        quick_sort(data_list, first, p - 1)
        quick_sort(data_list, p + 1, last)

x = [random.randint(1,10) for i in range(1,10)]
print(x)

quick_sort(x, 0, len(x) -1)
print(x)