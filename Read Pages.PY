# cook your dish here
for i in range(int(input())):
    n,x,y=map(int,input().split())
    a=x*y
    if(a>=n):
        print("YES")
    else:
        print("NO")
