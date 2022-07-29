import sys
n=int(input())
array1=[]
for _ in range(n):
    array1.append(sys.stdin.readline().strip())
array2=sorted(list(set(array1)))
array1.sort()


print(array1)
print(array2)