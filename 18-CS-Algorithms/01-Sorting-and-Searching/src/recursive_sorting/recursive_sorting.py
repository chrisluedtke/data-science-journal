def quicksort(ls): # O(n ^ 2) at worst, O(n * log(n)) on average
    if ls == []:
        return ls

    left, right = [], []
    pivot = ls[0]
    for item in ls[1:]:
        if pivot < item:
            left.append(pivot)
        else:
            right.append(pivot)

    return quicksort(left) + [pivot] + quicksort(right)


def merge(arr_a, arr_b):  # helper function
    merged_arr = []
    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] <= arr_b[0]:
            merged_arr.append(arr_a.pop(0))
        else:
            merged_arr.append(arr_b.pop(0))
    
    return merged_arr + arr_a + arr_b


def merge_sort(arr):  # O(n * log(n))
    if len(arr) < 2:
        return arr

    mid_i = len(arr) // 2
    left, right = merge_sort(arr[:mid_i]), merge_sort(arr[mid_i:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
