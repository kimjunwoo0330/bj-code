import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(x,y): # graph 선언할 때랑 안할때 차이
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(len(dx)):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    return graph[n-1][m-1]   

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))
print(bfs(0,0))







