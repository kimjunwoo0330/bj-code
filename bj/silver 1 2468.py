import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input().strip())
array1=[]
max_1=0
for _ in range(n):
    array1.append(list(map(int,input().split())))

def dfs(graph,x,y):
    if x < 0 or y < 0 or x >=n or y >=n:
        return False
    if graph[x][y]!=0:
        graph[x][y]=0
        dfs(graph,x+1,y)
        dfs(graph,x-1,y)
        dfs(graph,x,y+1)
        dfs(graph,x,y-1)
        return True
    return False

def fu1(array,l):
    for a in array:
        for j in range(n):
            if a[j] <= l:
                a[j]=0

for i in range(0,max(max(array1))):
    cnt=0
    array2=[item[:] for item in array1]
    fu1(array2,i)
    for k in range(n):
        for j in range(n):
            if dfs(array2,k,j)==True:
                cnt+=1
    max_1=max(cnt,max_1) 
print(max_1)