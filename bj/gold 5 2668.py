import sys
input=sys.stdin.readline
n=int(input())
gra=[]
array1=[0]
for _ in range(n):
    array1.append(int(input()))

def dfs(x,visited):
    a=array1[x]
    if visited[a]==0: 
        visited[a]=1
        check.append(a)
        dfs(a,visited)
    return check

for i in range(1,n+1):
    check=[]
    visited=[0]*(n+1)
    check.append(i)
    dfs(i,visited)
    if check.count(i)==2:
        gra.append(i)
        
print(len(gra))

for i in gra:
    print(i)