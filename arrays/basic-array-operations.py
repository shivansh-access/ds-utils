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


def print_all_the_elements_of_an_array(input_array):
    print("printing all the elements of an array")
    for i in range (0, len(input_array)):
        print(input_array[i])


def check_if_array_size_is_greater_than_five(input_array):
    size = len(input_array)
    if size > 5:
        return True
    else:
        return False


def check_if_the_array_size_is_greater_than_target(input_array, target):
    size = len(input_array)
    if size > target:
        return True
    else:
        return False
    

def check_if_the_array_size_is_greater_than_target_short_version(input_array, target):
    return len(input_array) > target


def sum_of_elements_in_array(input_array):
    result = 0
    for i in range (0, len(input_array)):
        result = result + input_array[i]
    return result


def product_of_elements_in_array(input_array):
    result = 1
    for x in range(0, len(input_array)):
        result = result * input_array[x]
    return result


def check_if_array_contains_5(input_array):
    for x in range(0, len(input_array)):
        v = input_array[x]
        if v == 5:
            return True
    return False

        
def check_if_array_contains_target(input_array, target):
    for i in range(0 , len(input_array)):
        if target == input_array[i]:
            return True
    return False     


#print(check_if_array_contains_target([6, 8, 4, 7, 3], 17))
#print(check_if_array_contains_5([8, 6, 4, 0, 4, 2, 5, 10, 12, 2]))
#print(print_first_element_of_the_array("5" "10"))
#print_array_elements(["I", "am", "ready"])
#print_array_elements([11, 32, 42, 90, 22, 10])
#print_last_element_of_the_array([1, 10, 16]) 
#print_all_the_elements_of_an_array([6, 1, 10])
#print(f"Array size is greater than 5? = {check_if_array_size_is_greater_than_five([5, 7, 8, 7])}")
#print(f"Array size is greater than 5? = {check_if_array_size_is_greater_than_five([5, 7, 8, 7, 9, 2, 0])}")
#print(f"Array size greater than the target? :{check_if_the_array_size_is_greater_than_target([5, 7, 9, 7, 4, 6], 4)}")
#print(f"Array size greater than the target? :{check_if_the_array_size_is_greater_than_target_short_version([5, 7, 9, 7, 4, 6], 4)}")
#print(f"The sum of the elments in array: {sum_of_elements_in_array([0, 9, 4, 3, 6, 8])}")
#print(f"The product of the elements in array: {product_of_elements_in_array([5, 6])}")
#print(f"product of_elements in array: {product_of_elements_in_array([5, 10, 10, 15])}")
#print(f"checking for {x} index having value as {v}"
