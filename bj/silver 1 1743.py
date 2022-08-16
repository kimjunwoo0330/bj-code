from collections import deque

def bfs(x,y):
    cnt=1
    visited[x][y]=0
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(len(dx)):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==1:
                visited[nx][ny]=0
                cnt+=1
                que.append((nx,ny))
    return cnt

n,m,k=map(int,input().split())
visited=[[0]*(m)for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    visited[a-1][b-1]=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]
max1=0

for i in range(n):
    for j in range(m):
        if visited[i][j]==1:
            max1=max(max1,bfs(i,j))

print(max1)