def binary_search(array, target):
    if target < array[0] or target > array[-1]:  # Early return if target is out of range
        return -1

    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)  # Bitwise shift instead of integer division

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
    
def binary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)
