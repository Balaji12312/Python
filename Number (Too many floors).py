n=int(input())
for i in range(n):
    x,y=map(int,input().split(" "))
    X=x//10
    Y=y//10
    if (x%10>0):
        X+=1
    if (y%10>0):
        Y+=1
    print(abs(Y-X))