x,y=map(int,input().split())
z=y*100//x
start=x
end=x*10

re=0
while start<=end:
    mid=(start+end)//2
    x1=mid
    y1=x1-x+y
    z1=y1*100//x1
    if z1 > z:
        re=x1-x
        end=mid-1
    else:
        start=mid+1
if re==0:
    print(-1)    
else:
    print(re)