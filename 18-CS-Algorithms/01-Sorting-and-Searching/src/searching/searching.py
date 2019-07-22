# STRETCH: implement Linear Search				
def linear_search(arr, target):
    
    # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
      return -1 # array empty
      
    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def test_binary_search_recursive(sorted_array, target, idx_min=0, idx_max=None):
    if not sorted_array[0] <= target <= sorted_array[-1]:
        return False
    if idx_max is None:
        idx_max = len(sorted_array) - 1
    
    idx_mid = (idx_min + idx_max) // 2

    if sorted_array[idx_mid] == target:
        return idx_mid
    elif target < sorted_array[idx_mid]:
        idx_max = idx_mid -1 
    elif sorted_array[idx_mid] < target:
        idx_min = idx_mid + 1

    return test_binary_search_recursive(sorted_array, target, idx_min, idx_max)
