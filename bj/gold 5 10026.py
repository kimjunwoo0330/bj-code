import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(graph,x,y,visited):
    if not visited[x][y]:
        visited[x][y]=True
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx < 0 or ny < 0 or nx>= n or ny>= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[x][y]!=graph[nx][ny]:
                continue
            if graph[x][y]==graph[nx][ny]:
                dfs(graph,nx,ny,visited)
        return True
    return False

def fu1(graph):
    visited=[[False]*n for _ in range(n)]
    re=0
    for i in range(n):
        for j in range(n):
            if dfs(graph,i,j,visited)==True:
                re+=1
    print(re,end=" ")

graph1=[]
graph2=[[] for _ in range(n)]

for _ in range(n):
    array1=input().strip()
    graph1.append(array1)
    for j in range(len(array1)):
        for i in array1[j]:
            k=i.replace("R","G")
            graph2[j].append(k)

fu1(graph1)
fu1(graph2)

