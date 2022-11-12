# Description: Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {
# 1, 2, …n} is missing and one number occurs twice in the array. Our task is to find these two numbers.
#
# Input
# [2, 3, 2, 1, 5]
# Output
# 4 2


def find_repeating_element(given_array):
    hashMap = {}

    for i in given_array:
        hashMap[i] = given_array.count(i)

    for i in hashMap:
        if hashMap[i] > 1:
            return i
    return -1


def find_missing_element(given_array):
    set1 = set(given_array)
    n = len(set1) + 1
    return n * (n + 1) // 2 - sum(set1)


array = [2, 3, 2, 1, 5]

print(find_missing_element(array), find_repeating_element(array))
