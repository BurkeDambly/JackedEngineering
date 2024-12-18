# File Descriptor: Basic demonstration of insertion sort.
# Author: Burke Dambly



"""
Swap take the values at two indecies in an array and swaps them, 
altering the actual values in the array.
"""
def swap(int_array, index1, index2):
    # Create a value for swapping two indicies
    swap_placeholder = 1000
    # Take the current number and store it
    swap_placeholder = int_array[index1]

    # Override the current number with the previous number 
    int_array[index1] = int_array[index2]

    # Move the current number back to the previous position
    int_array[index2] = swap_placeholder

"""
Insertion sort works by looking at each number and enumerating back in the 
list until it finds the correct location. 
O(n log n) Complexity for worst, average, and best.
"""
def insertion_sort(int_array_orignial):
    # Prevent alteration of orignal data
    int_array = int_array_orignial

   
    # Enumerate through the array
    for number_index in range(len(int_array)):

        # Create a copy of the current index to be altered
        current_number_index = number_index

        # Check for 0 index to prevent out of bounds error and if the current number is less than the previous number
        while int_array[current_number_index] < int_array[current_number_index-1] and current_number_index != 0:
            
            # Swap the previous with the current
            swap(int_array, current_number_index, current_number_index-1)

            # Decrement the current index to keep checking backward
            current_number_index -= 1

    # return the newly sorted copy of the original array   
    return int_array

"""
__name__ is a special variable that holds the name of the current module
In the top-level code environment, the value is __name__ is "__main__"
if an imported module, the vaue of __name__ is the module name
"""
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
    print(insertion_sort(arr))