# Quick sort in Python
# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as the pivot
    pivot = array[high]
    # Pointer for the greater element
    i = low - 1
    # Traverse through all elements and compare each element with the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If an element smaller than the pivot is found,
            # swap it with the greater element pointed to by i
            i = i + 1
            # Swapping element at i with element at j
            array[i], array[j] = array[j], array[i]
    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]
    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # elements smaller than the pivot are on the left,
        # elements greater than the pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

# Input a list of numbers separated by spaces
data = input("Enter a list of numbers separated by spaces: ").split()
data = [int(x) for x in data]
print("Unsorted Array")
print(data)
size = len(data)
print("The length of the data is:", size)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
