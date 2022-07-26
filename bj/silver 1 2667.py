# dfs 풀이
import sys
sys.setrecursionlimit(10**6)

n=int(input())

graph=[] # 정보를 저장할 공간 생성
array1=[]


def dfs(x,y):
    global count
    if x < 0 or y < 0 or x >= n or y >=n:
        return False

    if graph[x][y]==1: # 방문 안했다면
        graph[x][y]=0  # 방문 처리
        count+=1
        for i in range(len(dx)): # 깊게 방문하기
            dfs(x+dx[i],y+dy[i])
        return True

    return False # graph[x][y]==0인 경우

for _ in range(n): # 주어진 정보 저장
    graph.append(list(map(int,input().strip())))
    
# 움직일 수 있는 방향
dx=[0,0,1,-1]
dy=[1,-1,0,0]

result=0

for i in range(n):
    for j in range(n):
        count=0
        if dfs(i,j)==True:
            result+=1
            array1.append(count)
            
print(result)
array1.sort()
for i in array1:
    print(i)