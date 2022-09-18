# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    f=c+d+e
    g=a-b
    h=g-f
    if(h>=0):
        print("yes")
    else:
        print("no")
    
