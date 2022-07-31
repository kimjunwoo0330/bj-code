n=int(input())
start=0
end=n
result=0
while start <=end:
    mid=(start+end)//2
    k=mid**2
    if k < n:
        start=mid+1 
    else:
        result=mid
        end=mid-1
print(result)