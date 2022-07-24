# 선택 정렬 : 가장 작은 데이터와 맨  앞의 데이터를 바꾼다
array1=[3,5,2,1,4,8,7,9,6]

for i in range(len(array1)):
    min_index=i
    for j in range(i+1,len(array1)):
        if array1[min_index] > array1[j]:
            min_index = j
    array1[i],array1[min_index]=array1[min_index],array1[i]
print(array1)

# 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입한다 (스와핑을 계속 한다)
array2=[2,5,4,7,8,6,9,1,3]
for i in range(1,len(array2)):
    for j in range(i,0,-1):
        if array2[j] < array2[j-1]:
            array2[j],array2[j-1]=array2[j-1],array2[j]
        else:
            break
print(array2)

#퀵 정렬 : 기준(피벗)을 설정하고 큰 수와 작은 수를 교환한다

# 계수 정렬 : 각각의 데이터가 몇 번 등장 했는지 체크한다



