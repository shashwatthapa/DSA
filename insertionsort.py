def insertionSort(A,n):
    for  i in range(1,n):
        x = A[i]
        j = i-1
        while (j>-1 and A[j]>x):
            A[j+1] = A[j]
            j-=1
        A[j+1] = x
A = list(map(int,input("Enter the numbers: ").split()))
n = len(A)
insertionSort(A,n)
print(A)