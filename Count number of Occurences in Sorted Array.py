# Description - Given a sorted array arr[ ] and a number x, We have to count the occurrences of x in arr[ ].
# Input : [1, 1, 2, 2, 2, 2, 3] , x = 2
# Output : 4

# Linear Search

def count_occurrence(array, x):
    count = 0
    for i in array:
        if i == x:
        if i == x:
            count += 1
    return count


arr = [1, 1, 2, 2, 2, 2, 3]
key = int(input("Enter the element"))

result = count_occurrence(arr, key)
print(result)


# Binary Search

def count_occurrence_binary(array, x):
    left = 0
    right = len(array) - 1
    n = len(array)

    def first_index(left, right, array, x):

        if right >= left:
            mid = (left + right) // 2
            if (mid == 0 or x > array[mid - 1]) and array[mid] == x:
                return mid
            elif x > arr[mid]:
                return first_index(mid + 1, right, array, x)
            else:
                return first_index(left, mid - 1, array, x)

    def last_index(arr, low, high, x, n):
        if high >= low:
            mid = (low + high) // 2;

            if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
                return mid
            elif x < arr[mid]:
                return last_index(arr, low, (mid - 1), x, n)
            else:
                return last_index(arr, (mid + 1), high, x, n)
        return -1

    return [first_index(left, right, array, x), last_index(array, left, right, x, n)]


arr = [1, 1, 2, 2, 2, 2, 3]
# key = int(input("Enter the element:"))
key = 2
value = count_occurrence_binary(arr, key)

count_of_element = value[1] - value[0] + 1

print(count_of_element)
