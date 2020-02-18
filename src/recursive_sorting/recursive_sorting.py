# TO-DO: complete the helper function below to merge 2 sorted arrays
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def merge( left, right ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO

    left_side = 0
    right_side = 0
    merged_arr = []

    while left_side < len(left) and right_side < len(right):
        if left[left_side] <= right[right_side]:
            merged_arr.append(left[left_side])
            left_side = left_side + 1
        else:
            merged_arr.append(right[right_side])
            right_side = right_side + 1
    
    merged_arr.extend(left[left_side:])
    merged_arr.extend(right[right_side:])
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2
    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])

    return merge(left, right)

# print(merge_sort(arr1))

# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
