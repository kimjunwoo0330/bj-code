import sys
input=sys.stdin.readline
n,k=map(int,input().split())
array1=[]

for _ in range(n):
    array1.append(int(input().strip()))

start,end,ar=1,max(array1),0
# 막걸리의 중간값으로 주전자를 나눴을 때 나머지들의 합으로 경우 계산
while start<=end:
    mid=(start+end)//2
    num=sum(i//mid for i in array1)
    if num >=k:
        ar=mid
        start=mid+1
    else:
        end=mid-1 
print(ar)