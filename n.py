
def sum_of_target(nums, target):
    for i in range(len(nums) -1):
        if nums[i] + nums[i+1] == target:
            return [i,i+1]
            break
        else:
            continue
    
