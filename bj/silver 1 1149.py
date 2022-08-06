import sys
input=sys.stdin.readline
n=int(input())
rgb=[]
sumrgb=[(0,0,0)]*(n)
for _ in range(n):
    rgb.append(list(map(int,input().split())))
sumrgb[0]=(rgb[0][0],rgb[0][1],rgb[0][2])

for i in range(1,n):
    sumrgb[i]=(min(sumrgb[i-1][1],sumrgb[i-1][2])+rgb[i][0],min(sumrgb[i-1][0],sumrgb[i-1][2])+rgb[i][1],min(sumrgb[i-1][1],sumrgb[i-1][0])+rgb[i][2])
    
print(min(sumrgb[n-1]))