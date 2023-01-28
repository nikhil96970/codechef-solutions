# cook your dish here
t=int(input())
x=0
while(x<t):
    n,a,b=map(int,input().split())
    time=2*(180+n)
    c=a+b
    print(time-c)
    x+=1
