import sys
from bisect import bisect_left,bisect_right
input=sys.stdin.readline

def bisect_1(array,left,right):
    return bisect_right(array,right)-bisect_left(array,left)
    
n=int(input().strip())
array1=sorted(list(map(int,input().split())))

m=int(input().strip())
arraym=list(map(int,input().split()))

for i in arraym:
    print(bisect_1(array1,i,i),end=" ")