from bisect import bisect_left,bisect_right
n,x=map(int,input().split())
array1=list(map(int,input().split()))
a=bisect_left(array1,x)
b=bisect_right(array1,x)

if b-a > 0:
    print(b-a)
else:
    print(-1)