def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
        elif element > target:  # Only works if arr is sorted
            return -1

    return -1
    
def linear_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)
