# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d=a+b
    if(c>d):
        print("PLANEBUS")
    elif(d>c):
        print("TRAIN")
    elif(d==c):
        print("EQUAL")
