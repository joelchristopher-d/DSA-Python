def shellsort(arr):
    n = len(arr)
    increment = n//2
    while(increment>0):
        i = increment
        while i<n:
            temp = arr[i]
            j=i
            while(j>=increment):
                if temp<arr[j-increment]:
                    arr[j] = arr[j-increment]
                    print(j,j-increment)
                else:
                    break
                j-=increment
            arr[j] = temp
            i+=1
        increment //= 2
        
        
arr = [7, 6, 5, 4, 3, 2, 1,9,0]
shellsort(arr)
print(arr)
