import sys
input=sys.stdin.readline
# bfs 풀이는 deque을 이용한다
from collections import deque

n,m=map(int,input().split())

# 노드간의 정보를 담을 저장공간 생성
graph=[[] for _ in range(n+1)]

# 노드 사이의 연결관계를 저장
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리 및 횟수를 저장할 함수 생성
def bfs(graph,x,visit):
    que=deque()
    que.append(x)
    visit[x]=1
    while que:
        x=que.popleft()
        for i in graph[x]:   
            if visit[i] ==0: # x와 연결된 노드 중에 방문을 안 했다면
                visit[i]=visit[x]+1 # x+1 (깊이 처리)
                que.append(i) # 다시 que에 넣어서 반복 실행
    return sum(visit)-n 


min_1=[]
for i in range(1,n+1):
    visited=[0]*(n+1) # 각 케이스 별 방문을 기록하기 위하여 새로 생성
    min_1.append(bfs(graph,i,visited)) # 리턴 값을 저장

print(min_1.index(min(min_1))+1)