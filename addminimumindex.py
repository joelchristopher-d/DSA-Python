def addminimum(triangle):
    add=0
    index=0
    for i in range(len(triangle)):
        if len(triangle[i])>index+1:
            print(len(triangle[i]),index)
            index = index if triangle[i][index] < triangle[i][index+1] else index+1
        add+=triangle[i][index]
    return add

triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
addminimum(triangle)
