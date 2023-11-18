def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        diff = arr[high] - arr[low]
        pos = low + ((target - arr[low]) * (high - low)) // diff

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def interpolation_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)
