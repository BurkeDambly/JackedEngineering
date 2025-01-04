

def merge(left, right):
    a = []

    left_pointer = 0
    right_pointer = 0
    

    while(left_pointer < len(left) and right_pointer < len(right)):
        if(left[left_pointer]<right[right_pointer]):
            a.append(left[left_pointer])
            left_pointer+= 1

        else:
            a.append(right[right_pointer])
            right_pointer += 1
    
    a.extend(right[right_pointer:])
    a.extend(left[left_pointer:])

    return a
        


def mergeSort(int_arr):

    if(len(int_arr) <= 1):
        return int_arr
    
    middle = int(len(int_arr) / 2)
    left = int_arr[:middle]
    right = int_arr[middle:]
    

    left_sort = mergeSort(left)
    right_sort = mergeSort(right)

    return merge(left_sort, right_sort)


if __name__ == "__main__":
    int_array = [5, 4, 3, 1,2]
    print(mergeSort(int_array))