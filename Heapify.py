def heapify(arr, n, i):
    parent = i
    left_child = (i*2)+1
    right_child = (i*2)+2

    if (left_child < n and arr[left_child] > arr[parent]):
        parent = left_child

    if (right_child < n and arr[right_child] > arr[parent]):
        parent = right_child

    if (parent != i):
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr, n, parent)

def heap_sort(arr):
    size = len(arr)

    for i in range(size//2, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


arr = [int(item) for item in input("Enter your array: ").split()]
heap_sort(arr)
print(arr)
