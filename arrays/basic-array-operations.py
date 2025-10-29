def print_array_elements(input_arr):
    print(f"Working for array of length: {len(input_arr)}")
    print(f"Printing the array: {input_arr}")

    for i in range(0, len(input_arr)):
       print(f"Printing index: {i}")

    for i in range(0, len(input_arr)):     
       print(f"Printing element: {input_arr[i]}")


def print_first_element_of_the_array(input_arr):
    print(f"Printing the first element: {input_arr[0]}")


def print_last_element_of_the_array(input_arr):
    print(f"Printing the last element: {input_arr[len(input_arr) -1]}")


#print(print_first_element_of_the_array("5" "10"))
#print_array_elements(["I", "am", "ready"])
#print_array_elements([11, 32, 42, 90, 22, 10])
#print_last_element_of_the_array([1, 10, 16]) 