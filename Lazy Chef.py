# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    x=0
    x=a*b
    res=(x,c+a)
    y=min(res)
    print(y)
