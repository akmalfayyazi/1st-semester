def binary_search(arr, target, low, high):
    """
    Perform binary search recursively to find the target value in the given sorted list.

    Parameters:
        arr (list): The sorted list to be searched.
        target: The value to be searched for.
        low (int): The lower index of the search interval.
        high (int): The upper index of the search interval.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")