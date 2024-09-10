def recinsert(ind,arr):
    if ind==len(arr):return
    temp = arr[ind]
    j=ind-1
    while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
    arr[j+1]=temp
    recinsert(ind+1,arr)
        
arr = [10,9,8,7,6,5,4,3,2,1]
recinsert(1,arr)
print(arr)
