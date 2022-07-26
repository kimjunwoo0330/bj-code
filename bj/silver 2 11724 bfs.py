import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
count=0
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,x,visited):
    global count
    if not visited[x]:
        que=deque([x])
        visited[x]=True
        while que:
            a=que.popleft()
            for i in graph[a]:
                if not visited[i]:
                    que.append(i)
        count+=1

for i in range(1,n+1):
    bfs(graph,i,visited)
print(count)

