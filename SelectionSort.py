def Selectionsort(l):
    for i in range(len(l)):
        min_ind=i
        for j in range(i+1,len(l)):
            if l[min_ind]>l[j]:
                min_ind=j
        l[i],l[min_ind]=l[min_ind],l[i]
    return l
l=[5,4,1,8,9,2]
Selectionsort(l)
