a = list(map(int,input("Enter the numbers").split()))
for i in range(0,5):
    for j in range(i+1,5):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)