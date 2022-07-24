import sys
sys.setrecursionlimit(10**6)
while 1:
    w,h=map(int,input().split())
    if w==0 and h == 0:
        break
    graph=[]
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))

    dx=[1,1,1,0,0,-1,-1,-1]
    dy=[-1,0,1,1,-1,1,-1,0]

    def dfs(x,y):
        if x < 0 or y < 0 or x >= h or y >= w:
            return False
        if graph[x][y]==1:
            graph[x][y]=0
            for i in range(len(dx)):
                px=dx[i]+x
                py=dy[i]+y
                dfs(px,py)
            return True
        else:
            return False
    re=0
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                re+=1
    print(re)
            
