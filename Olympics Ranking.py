# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    x=a+b+c
    y=d+e+f
    if x>y:
        print(1)
    else:
        print(2)
