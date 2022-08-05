import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    # 0과 1을 각각 불러올 때 미리 저장할 공간을 생성
    # 중복해서 전의 결과를 이용하므로 dp를 사용한다
    d0=[0]*(n+2)
    d1=[0]*(n+2)
    d0[0]=1
    d1[1]=1
    for i in range(2,n+1): # 바텀 - 업 방식으로 구현
        d0[i]=d0[i-1]+d0[i-2]
        d1[i]=d1[i-1]+d1[i-2]
    print(d0[n],d1[n])