import sys
input=sys.stdin.readline
k,n=map(int,input().split())
array1=[]
for _ in range(k):
    array1.append(int(input()))
start=0
end=max(array1)
max_1=0
while start <= end:
    sum=0
    mid=(start+end)//2
    for i in array1:
        sum+=i//mid
    if sum >= n:
        max_1=max(max_1,mid)
        start=mid+1
    else:
        end=mid-1
print(max_1)
# start 값과 end값을 잘 설정해야한다 / 문제를 잘 읽어라 / yes or no 문제는 이진 탐색