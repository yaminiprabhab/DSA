def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Count inversions
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inv_count = merge_sort_and_count(arr, temp, left, mid)
    inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
    inv_count += merge_and_count(arr, temp, left, mid, right)
    
    return inv_count

def getInversions(arr, n):
    temp = [0] * n
    return merge_sort_and_count(arr, temp, 0, n - 1)
