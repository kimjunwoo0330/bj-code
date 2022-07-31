import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
graph=[]
for i in range(5):
    graph.append(input().split())

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def dfs(x,y,s):
    if len(s)==6:
        if s not in result:
            result.append(s)
        return 
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,s+graph[nx][ny])
result=[]

for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
print(len(result))

# += (누적합)과 + 를 잘 구별해서 이용하라