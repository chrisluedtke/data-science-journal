def selection_sort( arr ):  # O(n ^ 2)
    max_i = len(arr)
    for current_i in range(max_i - 1):
        min_val_i = current_i

        for i in range(current_i, max_i):  # find next smallest element
            if arr[i] < arr[min_val_i]:
                 min_val_i = i

        arr[current_i], arr[min_val_i] = arr[min_val_i], arr[current_i]  # swap

    return arr


def bubble_sort(arr):  # O(n ^ 2)
    swap_made = True
    while swap_made:
        swap_made = False
        for i in range(len(arr) - 1):
            if arr[i+1] < arr[i]:  # if next item less than current
                arr[i], arr[i+1] = arr[i+1], arr[i]  # swap
                swap_made = True

    return arr


def count_sort( arr, maximum=-1 ):

    return arr