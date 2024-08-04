def CountingSort(arr,maxval):
    counter = [0 for i in range(maxval+1)]
    for i in arr:
        counter[i]+=1
    start=0
    for i in range(len(counter)):
        while counter[i]>0:
            arr[start]=i
            start+=1
            counter[i]-=1
    return arr

arr=[5,3,2,3,6,1]
CountingSort(arr,max(arr))
