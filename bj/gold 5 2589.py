import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input().strip()))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(visited,x,y):
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(len(dx)):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx < 0 or ny < 0 or nx>=n or ny >= m:
                continue
            if graph[nx][ny]=="L" and visited[nx][ny]==0: # 땅이고 방문하지 않았다면
                visited[nx][ny]=visited[x][y]+1 # 방문 처리
                que.append((nx,ny)) 

    return visited
visited=[[0]*m for i in range(n)]
max_1=0
for i in range(n): 
    for j in range(m): # 좌표 전부 탐색
        if graph[i][j]=="L": # 땅인 경우로 한정
            visit=[x[:] for x in visited] # 방문 복사 생성
            visit[i][j]=1
            max_1=max(max(map(max,bfs(visit,i,j))),max_1) # 최단거리값 중 큰 것 저장
print(max_1-1)