import math

def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    left, right = 0, 0

    if target < arr[0] or target > arr[-1]:  # Early return if target is out of range
        return -1

    while right < n and arr[right] < target:
        left = right
        right += jump

    for i in range(left, min(right, n)):
        if arr[i] == target:
            return i

    return -1

def jump_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)
