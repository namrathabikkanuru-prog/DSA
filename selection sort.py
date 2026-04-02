
# selection sort :
# 153

def selection_sort(nums):
    n = len(nums)
    rotations = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
           if nums[min_idx] > nums[j]: 
             min_idx = j
             rotations += 1
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums, nums[0], rotations
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
print(selection_sort(nums))


# 414

def third_max(nums):
    n = len(nums)
    for i in range (n):
        min_index =i
        for j in range(i+1 , n):
            if nums[j] < nums[min_index]:
                min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums, nums[i-2]

nums = [3,2,1,4,3,1,4,5]
print(third_max(nums))
