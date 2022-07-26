import sys
from collections import deque
n,m,v=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(len(graph)):
    graph[i].sort()

def dfs(graph,x,visiteddfs):
    visiteddfs[x]=True
    print(x,end=" ")
    for i in graph[x]:
        if not visiteddfs[i]:
            dfs(graph,i,visiteddfs)

def bfs(graph,x,visitedbfs):
    que=deque([x])
    visitedbfs[x]=True
    while que:
        a=que.popleft()
        print(a,end=" ")
        for i in graph[a]:
            if not visitedbfs[i]:
                que.append(i)
                visitedbfs[i]=True

visiteddfs=[False]*(n+1)
visitedbfs=[False]*(n+1)

dfs(graph,v,visiteddfs)
print()
bfs(graph,v,visitedbfs)