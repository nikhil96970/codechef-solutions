# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    f=(d*10)+b
    e=(c*10)+a
    if(e>f):
        print("chefina")
    elif(f>e):
        print("chef")
    elif e==f:
        print("draw")
