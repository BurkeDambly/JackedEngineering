# File Descriptor: Basic demonstration of merge sort.
# Author: Burke Dambly
# & "C:/Users/burke/AppData/Local/Programs/Python/Python312/python.exe" -m pip install numpy
import numpy
print_enable = 0


"""
The merge function takes two arrays, sorts them and returns a combined sorted array.
The combine functionality works by using the correct assumption of being given 
two arrays that are already sorted. By doing this it can find all the positions
relative to the other list and then append the entire 'other' list once a single
one has had all the numbers placed.
"""
def merge(left_array, right_array):
    array_combined = []

    current_index_left = 0
    current_index_right = 0
    inserted_number_index = 0
    while(current_index_left < len(left_array) and current_index_right < len(right_array)):
        

        if(left_array[current_index_left] < right_array[current_index_right]):                         
            array_combined.append(left_array[current_index_left])
            current_index_left+=1
        
        else:              
            array_combined.append(right_array[current_index_right])
            current_index_right+=1
           
    array_combined.extend(right_array[current_index_right:])         
    array_combined.extend(left_array[current_index_left:])
            

    return array_combined
    
"""
Merge sort takes an array and breaks it into two halfs. These halfs are then recursively broken 
down into more halves until there is a single number. From there each broken half is re-combined in
sorted order. (Ex. 'left_sorted' is assigned to a called merge_sort(). merge_sort returns an array;
this array has been sorted all the way down until each array is in a single number).
"""
def merge_sort(int_array):
    
    if len(int_array) <= 1:
        return int_array

    middle = int(len(int_array)/2)
    left_array = int_array[:middle]
    right_array = int_array[middle:]

        
    left_sorted = merge_sort(left_array)
    right_sorted = merge_sort(right_array)

    if(print_enable):
        print(left_sorted, end=" ")
        print(right_sorted, end=" -> ")
        print(merge(left_sorted, right_sorted))
        
    return merge(left_sorted, right_sorted) 



if __name__ == "__main__":
    arr_even = [9, 8, 2, 1]
    arr_odd = [1, 2, 3, 4, 8, 7, 6]
    print(merge_sort(arr_even))