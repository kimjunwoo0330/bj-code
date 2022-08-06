# 최단거리는 왔던 곳을 다시 들리지 않는다
# 최단거리 방문기록은 bfs 이용한다
import sys
from collections import deque
input=sys.stdin.readline
f,s,g,u,d=map(int,input().split())
visited=[0]*(f+1)
a=[u,-d]
def bfs(s,f):
    que=deque()
    que.append(s)
    visited[s]=1
    while que:
        n=que.popleft()
        for i in range(2): # 상승과 하강에 따른 값 대입
            nx=n+a[i]
            if nx < 1 or nx >f:
                continue
            if visited[nx]==0:
                visited[nx]=visited[n]+1 
                que.append(nx)
    return visited[g] # 원하는 g층까지 도착하는데 걸린 횟수 리턴 
k=bfs(s,f)
if k >= 1: # g층에 도착을 했다면
    print(k-1)
else: # g층에 도착을 못 했다면
    print("use the stairs")