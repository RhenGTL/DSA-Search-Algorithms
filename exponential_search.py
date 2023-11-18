def binary_search(arr, target, left, right):
    if target < arr[left] or target > arr[right]:  # Early return if target is out of range
        return -1

    while left <= right:
        mid = left + ((right - left) >> 1)  # Bitwise shift instead of integer division

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    n = len(arr)

    while i < n and arr[i] <= target:
        i <<= 1  # Bitwise shift instead of multiplication

    return binary_search(arr, target, i >> 1, min(i, n) - 1)

def exponential_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)
