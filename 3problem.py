def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    merged_arr += arr1[i:]
    merged_arr += arr2[j:]
    return merged_arr

n = int(input("Enter the size of the first array: "))
arr1 = list(map(int, input("Enter the first sorted array: ").split()))
m = int(input("Enter the size of the second array: "))
arr2 = list(map(int, input("Enter the second sorted array: ").split()))

merged_arr = merge_sorted_arrays(arr1, arr2)
print("Merged sorted array: ", merged_arr)