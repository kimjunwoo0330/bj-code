import sys
input=sys.stdin.readline
n,m=map(int,input().split())
array1=sorted(list(map(int,input().split())))

start=0
end=max(array1)

re=0
while start<=end:   
    mid=(start+end)//2 
    sum=0
    for i in array1:
        if i>mid: 
            sum+=i-mid # array 더하는것과 같다
    if sum <m:
        end=mid-1
    else:
        re=mid
        start=mid+1

print(re)