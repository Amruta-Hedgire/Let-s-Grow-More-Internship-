import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)

def deterministic_quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Choose the last element as the pivot
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort1(less) + [pivot] + deterministic_quick_sort1(greater)

# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Measure execution time
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sorted_array = sort_function(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, sorted_array

if __name__ == "__main__":
    random.seed(42)  # For consistent results with randomized Quick Sort
    arr = [random.randint(1, 1000) for _ in range(1000)]
    det_time, det_sorted = measure_execution_time(deterministic_quick_sort, arr.copy())
    det_time1, det_sorted1 = measure_execution_time(deterministic_quick_sort1, arr.copy())
    rand_time, rand_sorted = measure_execution_time(randomized_quick_sort, arr.copy())

    print("Deterministic Quick Sort (low pivot)")
    print("Execution Time:", det_time, "seconds")
    # Uncomment the next line to print the sorted array:
    # print("Sorted Array:", det_sorted)

    print("Deterministic Quick Sort (high pivot)")
    print("Execution Time:", det_time1, "seconds")
    # Uncomment the next line to print the sorted array:
    # print("Sorted Array:", det_sorted1)

    print("\nRandomized Quick Sort:")
    print("Execution Time:", rand_time, "seconds")
    # Uncomment the next line to print the sorted array:
    # print("Sorted Array:", rand_sorted)
