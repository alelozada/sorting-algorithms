def shell_sort(arr, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2


data = [8, 12, 1, 3, 5]
size = len(data)
shell_sort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
