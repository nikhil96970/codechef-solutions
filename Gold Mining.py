# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d=0
    d=(a+1)*c
    if(d>=b):
        print("yes")
    else:
        print("no")
