def print_array_elements(input_arr):
    print(f"Working for array of length: {len(input_arr)}")
    print(f"Printing the array: {input_arr}")

    for i in range(0, len(input_arr)):
        print(f"Printing index: {i}")

    for i in range(0, len(input_arr)):     
       print(f"printing elements {input_arr[i]}")


print_array_elements(["I", "am", "ready"])
print_array_elements([11, 32, 42, 90, 22, 10])  