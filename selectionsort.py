def selectionSort(A,n):
    for i in range(0,n):
        k = i
        for j in range(i+1,n):
            if (a[j]<a[k]):
                k = j
        temp = a[i]
        a[i] = a[k]
        a[k] = temp
a = list(map(int,input("Enter the elements: ").split()))
b = len(a)
selectionSort(a,b)
print(a)