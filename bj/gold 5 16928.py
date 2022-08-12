import sys
from collections import deque
input=sys.stdin.readline

visited=[0]*101
sadary,sadarymove=deque(),deque()
snake,snakemove=deque(),deque()
dx=[1,2,3,4,5,6]

def bfs(x,visited):
    que=deque()
    que.append(x)
    while que:
        x=que.popleft()
        for i in range(len(dx)):
            nx=x+dx[i]
            if nx>100:
                continue
            if visited[nx]==0:
                if nx in sadary:
                    a=sadary.index(nx)
                    if visited[sadarymove[a]]==0:
                        visited[nx]=visited[x]+1
                        visited[sadarymove[a]]=visited[nx]
                        que.append(sadarymove[a])
                if nx in snake: 
                    b=snake.index(nx)
                    if visited[snakemove[b]]==0:
                        visited[nx]=visited[x]+1
                        visited[snakemove[b]]=visited[nx]
                        que.append(snakemove[b])
                else:
                    visited[nx]=visited[x]+1
                    que.append(nx)
    return visited[100]

n,m=map(int,input().split())

for _ in range(n):
    a,b=map(int,input().split())
    sadary.append(a)
    sadarymove.append(b)

for _ in range(m):
    a,b=map(int,input().split())
    snake.append(a)
    snakemove.append(b)

print(bfs(1,visited))