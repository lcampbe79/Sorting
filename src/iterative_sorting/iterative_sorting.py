# import random

# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    
    return arr
# print(selection_sort(arr1))
# print(selection_sort(arr3))

# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr