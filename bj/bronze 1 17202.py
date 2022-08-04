import sys
input=sys.stdin.readline
a=list(map(int,input().strip()))
b=list(map(int,input().strip()))
graph=[]

for i in range(8):
    graph.append(a[i])
    graph.append(b[i])

while len(graph)>2:
    array2=[]
    for i1 in range(len(graph)-1):
        array2.append((graph[i1]+graph[i1+1])%10)
    graph=array2
print(str(graph[0])+str(graph[1]))
    