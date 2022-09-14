# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split(' '))
    if(a or b or c or d == 1):
        print("OUT")
    else:
        print("IN")
