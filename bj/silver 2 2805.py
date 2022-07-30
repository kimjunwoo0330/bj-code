import sys
input=sys.stdin.readline
n,m=map(int,input().split())
array1=list(map(int,input().split()))
start,end,re=0,max(array1)-1,0

while start <= end:
    count=0
    mid=(start+end)//2
    for i in array1:
        if i > mid:
            count+=i-mid
    if m <= count:
        re=mid
        start=mid+1
    else:
        end=mid-1
print(re)
