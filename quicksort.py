def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while i < j:
        while i < h and A[i] <= pivot:
            i += 1
        while j > l and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quickSort(A, l, h):
    if l < h:
        j = partition(A, l, h)
        quickSort(A, l, j - 1)
        quickSort(A, j + 1, h)

a = list(map(int, input("Enter the numbers: ").split()))
quickSort(a, 0, len(a) - 1)
print(a)
