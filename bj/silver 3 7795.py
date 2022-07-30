import sys
from bisect import bisect_left
input=sys.stdin.readline
for _ in range(int(input().strip())):
    a,b=map(int,input().split())
    arraya=sorted(list(map(int,input().split())))
    arrayb=sorted(list(map(int,input().split())))
    count=0
    for i in arraya:
        count+=bisect_left(arrayb,i)
    print(count)