import sys
input=sys.stdin.readline
n=int(input())
array1=list(map(int,input().split()))
dp=[0]*(n)
dp[0]=array1[0]
# 직전의 합이 0보다 작으면은 이어서 더하지 않는다
for i in range(1,n):
    if dp[i-1]>=0:
        dp[i]=dp[i-1]+array1[i]
    else:
        dp[i]=array1[i]

print(max(dp))