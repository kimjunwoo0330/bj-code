# 좀 더 쉽게 풀어보자
n=int(input())
d=[0]*(n+3)
d[2]=1
d[3]=1
for i in range(4,n+1):
    if i%3==0:
        a=d[i//3]
    else:
        a=99999999999
    if i%2==0:
        b=d[i//2]
    else:
        b=99999999999
    if True:
        c=d[i-1]
    d[i]=min(a,b,c)+1
print(d[n])