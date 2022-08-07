import sys
input=sys.stdin.readline
dp=[]
n=int(input())
for _ in range(n):
    dp.append(list(map(int,input().split()))) 
# 위의 숫자를 피라미드 형식으로 아래로 더함 (dp사용)
for i in range(1,n):
    for j in range(len(dp[i])):
        if j==0: # 맨 앞의 경우 바로 위의 숫자와 합으로 결정
            dp[i][j]=dp[i-1][0]+dp[i][j]
        elif j==len(dp[i])-1: # 맨 뒤의 경우도 마찬가지
            dp[i][j]=dp[i-1][j-1]+dp[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+dp[i][j] # 위 양 옆의 두 숫자 중 큰 것을 택
print(max(dp[n-1]))