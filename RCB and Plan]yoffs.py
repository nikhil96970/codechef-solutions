# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    d=1
    w=2
    c=z*w
    if(c+x>=y):
        print("yes")
    else:
        print("no")
