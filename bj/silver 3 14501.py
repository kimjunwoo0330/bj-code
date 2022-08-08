import sys
input=sys.stdin.readline
n=int(input())
d,day,pay=[0]*(n+1),[0]*(n+1),[0]*(n+1)
for i in range(n):
    day[i],pay[i]=map(int,input().split())
#탑다운 방식으로 풀이 진행
for i in range(n-1,-1,-1): # 뒤에서부터 생각
    if day[i]+i >n: # 날짜가 넘어가면
        d[i]=0      # 그 위치에서의 최대값은 0
    else: # 처리가능한 날짜면
        d[i]=pay[i]+max(d[day[i]+i:]) # 최대합은 전 값 합 최대 + 위치의 합 

print(max(d))
