import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,visited):
    for i in graph[x]:
        if visited[i]==0:
            visited[i]=visited[x]+1
            dfs(i,visited) 
    if max(visited)==4:
        print(1)

visited=[0]*n
for i in range(n):
    a=dfs(i,visited)
    if a ==4:
        print(1)
        exit()
print(0)