def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


def max_heapify(tree, i):
    l = left(i)
    r = right(i)
    if l <= len(tree) and tree[l - 1] > tree[i - 1]:
        largest = l
    else:
        largest = i

    if r <= len(tree) and tree[r - 1] > tree[largest - 1]:
        largest = r

    if largest != i:
        tree[i - 1], tree[largest - 1] = tree[largest - 1], tree[i - 1]
        max_heapify(tree, largest)
    return tree


def build_max_heap(A):
    for i in range(len(A) // 2, 0, -1):
        A = max_heapify(A, i)
    return A


def heap_sort(A):
    sorted_arr = []
    A = build_max_heap(A)
    for i in range(len(A), 0, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        sorted_arr.append(A[i - 1])
        A = A[:len(A) - 1]
        A = max_heapify(A, 1)
    return sorted_arr[::-1]


if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heap_sort(A))
