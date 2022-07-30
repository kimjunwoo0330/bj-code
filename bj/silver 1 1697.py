from collections import deque
n,k=map(int,input().split())
visited=[0]*100001

def bfs(a):
    que=deque()
    que.append(a)
    while que:
        x=que.popleft()
        if x==k:
            return visited[k]
        for i in (x+1,x-1,x*2):
            if 0<= i <= 100000 and visited[i]==0:
                visited[i]=visited[x]+1
                que.append(i)

print(bfs(n))