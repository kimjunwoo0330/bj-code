import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
max1=0
def dfs(x,y):
    global max1
    global num
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y]==1:
        num+=1
        graph[x][y]=0
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        max1=max(max1,num)
        return True
    return False
re=0
for i in range(n):
    for j in range(m):
        num=0
        if dfs(i,j)==True:
            re+=1
if re > 0:
    print(re)
    print(max1)
else:
    print(0)
    print(0)
