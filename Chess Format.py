# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=range(3,11)
    d=range(11,61)
    e=a+b
    if(e<3):
        print("1")
    elif(e in c):
        print("2")
    elif(e in d):
        print("3")
    else:
        print("4")
