def Partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def QuickSort(arr,low,high):
    if low<high:
        pi = Partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
        
arr=[5,7,6,9,4,8,1,2,3,11,10]
low=0
high=len(arr)-1
QuickSort(arr,low,high)
print(arr)
