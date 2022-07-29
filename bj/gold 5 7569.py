import sys
from collections import deque
m,n,h=map(int,sys.stdin.readline().split()) # 가 세 높 

graph=[[] for _ in range(h)] # 깊이 먼저 선언 
visited=[[[False]*m for _ in range(m)] for __ in range(h)]
for i in range(h):
    for i2 in range(n):
        graph[i].append(list(map(int,sys.stdin.readline().split())))

dx=[0,0,1,-1,0,0]
dy=[0,0,0,0,1,-1]
dz=[1,-1,0,0,0,0]

def bfs(z,x,y):
    que=deque()
    que.append((z,y,x))
    while que:
        z,y,x=que.popleft()
        visited[z][y][x]=True
        if graph[z][y][x]==1:
            for i in range(len(dx)):
                kx=x+dx[i]
                ky=y+dy[i]
                kz=z+dz[i]
                if kx < 0 or kz <0 or ky < 0 or kz >= h or ky >= n or kx >= m:
                    continue
                if graph[kz][ky][kx]==-1:
                    visited[kz][ky][kx]=True
                    continue
                
   
print(graph[1][1][2])
bfs(1,1,2)

