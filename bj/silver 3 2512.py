import sys
input=sys.stdin.readline
n=int(input().strip())
array1=list(map(int,input().split()))
m=int(input().strip())
start=0
end=max(array1)

while start <=end:
    sum=0
    mid=(start+end)//2
    for i in array1:
        if i > mid:
            sum+=mid
        else:
            sum+=i
    if sum > m:
        end=mid-1
    else :
        start=mid+1
print(end)