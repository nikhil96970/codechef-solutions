# cook your dish here
for i in range(int(input())):
    x,y,z,p=map(int,input().split())
    if((x+y)>=p or (x+z) >=p or (y+z) >=p):
        print("YES")
    else:
        print("no")
