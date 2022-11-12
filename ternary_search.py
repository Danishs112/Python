# iterative approach

# Time Complexity = O(log3 N)

def ternary_search(left, right, target_element, given_array):
    while right >= left:

        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if given_array[mid1] == target_element:
            return mid1

        if given_array[mid2] == target_element:
            return mid2

        elif target_element < given_array[mid1]:
            right = mid1 - 1

        elif target_element > given_array[mid2]:
            left = mid2 + 1

        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
key = int(input("Enter the Element:"))
result = ternary_search(0, len(array) - 1, key, array)

print(result)


# recursion approach

def ternary_search_recursion(left, right, ele, arr):
    if right >= left:

        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == ele:
            return mid1

        elif arr[mid2] == ele:
            return mid2

        elif ele < arr[mid1]:
            return ternary_search_recursion(left, mid1 - 1, ele, arr)

        elif ele > arr[mid2]:
            return ternary_search_recursion(mid2 + 1, right, ele, arr)

        else:
            return ternary_search_recursion(mid1 + 1, mid2 - 1, ele, arr)

    return -1


given_array = [2, 3, 4, 5, 6, 7, 8, 9, 10]
key = int(input("Enter the Element:"))
result = ternary_search_recursion(0, len(given_array) - 1, key, given_array)

print(result)
