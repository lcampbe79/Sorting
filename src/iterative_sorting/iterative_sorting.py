import random

# # TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = random.sample(range(200), 50)

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
print(selection_sort(arr1))
print(selection_sort(arr2))
print(selection_sort(arr3))
print(selection_sort(arr4))


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = random.sample(range(200), 50)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Starts the comparison
    for i in range(0, len(arr) -1):
        #comparing inside the first for loop range
        for j in range(0, len(arr) -1):
            if arr[j + 1] < arr[j]:
                #swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(arr1))
print(bubble_sort(arr2))
print(bubble_sort(arr3))
print(bubble_sort(arr4))


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr