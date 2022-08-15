import sys
input=sys.stdin.readline
from collections import deque
def dfs(x):
    global cnt
    que=deque()
    que.append(x)
    visited[x]=True
    while que:
        x=que.popleft()
        for i in graph[x]:
            if visited[i]==False:
                visited[i]=True
                cnt+=1
                que.append(i)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
sum=deque()
sum.append(0)
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)


for i in range(1,n+1):
    visited=[False]*(n+1)
    cnt=0
    dfs(i)
    sum.append(cnt)
    
m=max(sum)
k=[i for i,v in enumerate(sum) if v==m]
k.sort()
for i in k:
    print(i,end=" ")