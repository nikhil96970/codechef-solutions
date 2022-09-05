for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    d=a+c
    if(b>=d):
        print("Yes")
    else:
        print("No")
