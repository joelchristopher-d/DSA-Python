def InsertionSort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j=i-1
        while(j>=0 and arr[j]>val):
            print(arr)
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=val
    return arr

l=[5,4,1,8,9,2]
print(InsertionSort(l))
