import random

def quicksort(arr, start, stop):
    if start < stop:
        # pivotindex is the index where the pivot lies in the array
        pivotindex = partitionrandom(arr, start, stop)
        # At this stage, the array is partially sorted around the pivot.
        # Separately sorting the left half of the array and the right half of the array.
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)

def partitionrandom(arr, start, stop):
    # Generating a random number between the starting index of the array and the ending index of the array.
    randpivot = random.randrange(start, stop)
    # Swapping the starting element of the array and the pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr, start, stop):
    pivot = start  # pivot
    i = start + 1  # a variable to memorize where the partition in the array starts from.
    for j in range(start + 1, stop + 1):
        # If the current element is smaller or equal to the pivot, shift it to the left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot

if __name__ == "__main__":
    array = [11, 7, 8, 9, 1, 5]
    print("Unsorted array: ")
    print(array)
    print("The length is:", len(array))  # Length is 6
    quicksort(array, 0, len(array) - 1)
    print("The sorted array is: ")
    print(array)
