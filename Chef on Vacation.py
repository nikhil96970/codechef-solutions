# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d=a+b
    if(d>c):
        print("no")
    else:
        print("yes")
