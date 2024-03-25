# QUESTION 5

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low

def lower_bound(arr, x):
    return binary_search(arr, x)

def upper_bound(arr, x):
    index = binary_search(arr, x)
    if index == len(arr) or arr[index] != x:
        return index
    else:
        while index + 1 < len(arr) and arr[index + 1] == x:
            index += 1
        return index + 1

def is_present(arr, x):
    index = binary_search(arr, x)
    if index == len(arr) or arr[index] != x:
        return False
    else:
        return True

arr = [1, 2, 2, 3, 0, 7, 5, 5]
x = 4

print("Lower bound of x:", lower_bound(arr, x))
print("Upper bound of x:", upper_bound(arr, x))
print("x is present:", is_present(arr, x))