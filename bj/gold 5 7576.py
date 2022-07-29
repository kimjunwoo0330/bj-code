import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[]
que=deque()

for i in range(m):
    array1=list(map(int,sys.stdin.readline().split()))
    graph.append(array1)
    for i2 in range(len(array1)):
        if array1[i2]==1:
            que.append([i,i2])
            
dx=[0,0,1,-1]
dy=[1,-1,0,0]

while que:
    x,y=que.popleft()
    for i in range(len(dx)):
        nx=dx[i]+x
        ny=dy[i]+y
        if nx<0 or ny < 0 or nx>=m or ny >=n:
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=graph[x][y]+1
            que.append([nx,ny])
day=0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    day=max(day,max(i))
print(day-1)
