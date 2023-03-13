# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split(' '))
    c=a*1.07
    if(b<=c):
        print("YES")
    else:
        print("NO")
