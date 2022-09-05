# cook your dish here
for i in range (int(input())):
    a,b=map(int,input().split(' '))
    c,d=map(int,input().split(' '))
    if(c>=a and d>=b):
        print("POSSIBLE")


    else:
        print("IMPOSSIBLE")
