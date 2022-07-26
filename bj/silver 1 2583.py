import sys
sys.setrecursionlimit(10**6)
m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
array_1=[]
for _ in range(k):
    a,b,c,d=map(int,input().split())
    for i in range(b,d):
        for j in range(a,c):
            graph[i][j]=1

def dfs(x,y):
    global count
    global array_1
    if x < 0 or y < 0 or x >= m or y>=n:
        return False
    if graph[x][y]==0:
        count+=1
        graph[x][y]=1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True

    return False
result=0
for i in range(m):
    for j in range(n):
        count=0
        if dfs(i,j)==True:
            result+=1
            array_1.append(count)
print(result)
array_1.sort()
for i in array_1:
    print(i,end=" ")