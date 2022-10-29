def merge_sort(arr):

    if len(arr)<=1: # O(1)
        return 

    mid = len(arr)//2 # O(1)

    left_arr = arr[:mid] # O(1)
    right_arr = arr[mid:] # O(1)

    print(left_arr, right_arr) # O(1)

    merge_sort(left_arr) # O(n)
    merge_sort(right_arr) # O(n)

    left_index = 0 # O(1)
    right_index = 0 # O(1)
    arr_index = 0 # O(1)

    while left_index < len(left_arr) and right_index < len(right_arr): # O(n^2)

        if left_arr[left_index] < right_arr[right_index]: # O(1)
            arr[arr_index] = left_arr[left_index] # O(1)
            left_index += 1 # O(1)
        
        else:
            arr[arr_index] = right_arr[right_index] # O(1)
            right_index += 1 # O(1)
        
        arr_index += 1 # O(1)
    
    if left_index < len(left_arr): # O(1)
        del arr[arr_index:] # O(log n)
        arr += left_arr[left_index:] # O(1)

    elif right_index < len(right_arr): # O(1)
        del arr[arr_index:] # O(log n)
        arr += right_arr[right_index:] # O(1)

    return arr # O(1)

# Time complexity: 

print(merge_sort([8, 12, 1, 3, 5]))