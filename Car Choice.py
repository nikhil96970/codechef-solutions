# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    e=c/a
    f=d/b
    if(e<f):
        print("-1")
    elif(f<e):
        print("1")
    elif(e==f):
        print("0")
