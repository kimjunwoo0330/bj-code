import sys
data=[]
for _ in range(int(input())):
    data.append(sys.stdin.readline().split())

data=sorted(data,key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
print(data)
for i in data:
    print(i[0])