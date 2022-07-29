import sys
input=sys.stdin.readline

def bisect(array,target,start,end):
    if start > end:
        return 0
    mid=(end+start)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return bisect(array,target,start,mid-1)
    else:
        return bisect(array,target,mid+1,end)

n=int(input().strip())
array1=sorted(list(map(int,input().split())))

m=int(input().strip())
array2=list(map(int,input().split()))

for i in array2:
    print(bisect(array1,i,0,n-1))