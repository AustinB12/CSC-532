def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

def my_heap_sort(arr: list[int]):
    assert isinstance(arr, list), "Input must be a list"

    if len(arr) < 2:
        # Lists of size 0 and 1 are always sorterd
        return arr
    
    # Convert array to a min Heap (implemented in an array)
    min_heap = []

    # Find the min value, that's the root of the heap
    min_value = min(arr)

    # index 0 = root I.E. minimum value element
    min_heap.append(min_value)
    # TODO finish this

    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)

test_lists = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [2, 1, 6, 8, 2, 4, 2, 4],
    [2, 2, 2, 2, 2, 2, 2],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for test in test_lists:
    print(my_heap_sort(test))
