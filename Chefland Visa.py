# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    if(b>=a and d>=c and e>=f):
        print("YES")
    else:
        print("NO")
