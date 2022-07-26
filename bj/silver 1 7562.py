from collections import deque
import sys
dx=[2,2,1,1,-1,-1,-2,-2]
dy=[1,-1,2,-2,2,-2,1,-1]
def bfs(a,b,c,d):
    que=deque()
    que.append((a,b))
    if a==c and b==d:
        return 0
    while que:
        x,y=que.popleft()
        for k in range(8):
            nx=dx[k]+x
            ny=dy[k]+y
            if nx < 0 or ny < 0 or nx>=i or ny >= i :
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    return graph[c][d]

for _ in range(int(sys.stdin.readline())):
    i=int(sys.stdin.readline())
    graph=[[0]*i for _ in range(i)]
    a,b=map(int,sys.stdin.readline().split())
    c,d=map(int,sys.stdin.readline().split())
    print(bfs(a,b,c,d))
