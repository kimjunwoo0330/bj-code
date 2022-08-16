from collections import deque
import copy
def bfs():
    global min1
    que=deque()
    graph1=copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph1[i][j]==2:
                que.append((i,j))
    while que:
        x,y=que.popleft()
        for i in range(len(dx)):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and graph1[nx][ny]==0:
                graph1[nx][ny]=2
                que.append((nx,ny))
    re=0
    for i in range(n):
        for j in range(m):
            if graph1[i][j]==0:
                re+=1

    min1=max(min1,re)

def wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            #백 트레킹 / 재귀 호출 이후 다시 초기화 시킨다
            if graph[i][j]==0:
                graph[i][j]=1
                wall(cnt+1)
                graph[i][j]=0
n,m=map(int,input().split())
graph=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

min1=0
wall(0)
print(min1)