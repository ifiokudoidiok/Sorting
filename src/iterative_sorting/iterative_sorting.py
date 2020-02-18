# TO-DO: Complete the selection_sort() function below 
# 1. Start with current index = 0

# 2. For all indices EXCEPT the last index:

#     a. Loop through elements on right-hand-side 
#     of current index and find the smallest element

#     b. Swap the element at current index with the
#     smallest element found in above loop
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
          
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through the whole array
    for index in range(len(arr)):
        # compare the number next to the first (index + 1) until you loop through the whole array
        for compared_num in range(index +1, len(arr)):
            # if lhs > rhs
            if arr[index] > arr[compared_num]:
                #swap
                arr[index],arr[compared_num] =arr[compared_num], arr[index] 
    #return array            
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr