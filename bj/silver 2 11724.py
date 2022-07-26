import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if not visited[x]:
        visited[x]=True
        for i in graph[x]:
            dfs(i)
        return True
    return False

re=0
for i in range(1,n+1):
    if dfs(i)==True:
        re+=1

print(re)
