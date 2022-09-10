# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    d=a-c
    if(b>=d):
        print("PASS")
    else:
        print("FAIL")
