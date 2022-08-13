n=int(input())
length=list(map(int,input().split())) 
price=list(map(int,input().split())) 

sum1=0
min_price=price[0]

for i in range(n-1):
    if price[i]<min_price:
        min_price=price[i]
    sum1+=min_price*length[i] 
    
print(sum1)
