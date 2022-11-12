# iterative approach

def binary_search(array, target_ele):
    left = 0
    right = len(array) - 1
    mid = 0

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target_ele:
            return array[mid]

        if array[mid] > target_ele:
            right = mid - 1

        else:
            left = mid + 1

    return - 1


arr = [2, 3, 4, 5, 6, 7, 8, 9]
ele = int(input("Enter the element:"))

result = binary_search(arr, ele)

if result != -1:
    print("Element is present on the array at index", str(result))
else:
    print("Element is not present on the array")