n,m=map(int,input().split()) #세로, 가로
graph=[]
for _ in range(n):
    graph.append(list(input().strip()))

def dfs_x(x,y):
    if x < 0 or y < 0 or x >=n or y >=m:
        return False

    if graph[x][y]=="|":
        graph[x][y]= 0
        dfs_x(x+1,y)
        return True
        
    return False

def dfs_y(x,y):
    if x < 0 or y < 0 or x >=n or y >=m:
        return False

    if graph[x][y]=="-":
        graph[x][y]= 0
        dfs_y(x,y+1)
        return True

    return False
    

result=0
for i in range(n):  
    for j in range(m):
        if graph[i][j]=="-":
            dfs_y(i,j)
            result+=1
        elif graph[i][j]=="|":
            dfs_x(i,j)
            result+=1
        
print(result)
