def linear_search(arr,target_element):

    for index in range(len(arr)):

        if arr[index] == target_element:
            return index

        return -1


arr =[1,2,43,46,32,546]
input_number = input("Enter the Number:")
x = linear_search(arr,input_number)
print(input_number)