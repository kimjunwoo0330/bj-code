from os import stat
import sys
input=sys.stdin.readline

def fuction1(array,target,start,end):
    while start <= end:
        mid=(start+end)//2
        if array[mid] == target:
            return print("yes",end=" ")
        elif array[mid] > target:
            end=mid-1
        else:
            start=mid+1
    return print("no",end=" ")

n=int(input().strip())
arrayn=sorted(list(map(int,input().split())))
m=int(input().strip())
arraym=list(map(int,input().split()))

for i in arraym:
    fuction1(arrayn,i,0,n-1)