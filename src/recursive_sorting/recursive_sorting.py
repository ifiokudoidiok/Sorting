# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr

'''[1,2,4,45,4] [1],[2]...
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled

- Implement `merge_sort()` in `recursive_sorting.py`. It's recommended that you use...
  - A recursive function that handles dividing the array (or subarray) in half
  - A helper function that handles merging sorted pieces back together
'''

def merge_function(left,right):
    elements = len(left) + len(right)
    sorted_result = []
    index_left = 0
    index_right = 0

    while len(sorted_result) < elements:
        if left[index_left] <= right[index_right]:
            sorted_result.append(left[index_left])
            index_left += 1
        else:
            sorted_result.append(right[index_right])
            index_right += 1
        if index_left == len(left):
            sorted_result += right[index_right:]
            break
        elif index_right == len(right):
            sorted_result += left[index_left:]
            break
    return sorted_result
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <=1:
        return arr
    else:
        middle = len(arr) //2
        left, right = arr[:middle], arr[middle:]
        return merge_function(merge_sort(left), merge_sort(right))
    return arr

print(merge_sort([1,94,5,2,8]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
