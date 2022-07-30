import sys
input = sys.stdin.readline

def de(array,target,start,end): #이분 탐색
    while start <= end:
        mid =(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid] > target:
            end=mid-1
        else:
            start=mid+1
    return 0

for _ in range(int(input().strip())):
    n=int(input().strip())
    array1=sorted(list(map(int,input().split())))
    m=int(input().strip())
    array2=list(map(int,input().split()))

    for i in array2:
        print(de(array1,i,0,n-1))