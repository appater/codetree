n = int(input())
arr = [0] + list(map(int, input().split()))

def heap_sort(arr):
    num_elements = len(arr) - 1

    for i in range(num_elements // 2, 0, -1):
        heapify(arr, num_elements, i)

    for i in range(num_elements, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i - 1, 1)

def heapify(arr, heap_size, parent_idx):
    largest_idx = parent_idx  
    left_child_idx = parent_idx * 2
    right_child_idx = parent_idx * 2 + 1

    if left_child_idx <= heap_size and arr[left_child_idx] > arr[largest_idx]:
        largest_idx = left_child_idx

    if right_child_idx <= heap_size and arr[right_child_idx] > arr[largest_idx]:
        largest_idx = right_child_idx

    if largest_idx != parent_idx:
        arr[parent_idx], arr[largest_idx] = arr[largest_idx], arr[parent_idx]
        heapify(arr, heap_size, largest_idx)

heap_sort(arr)

print(*arr[1:])