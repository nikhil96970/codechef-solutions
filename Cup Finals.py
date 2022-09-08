# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    result=a-b
    if(c>=abs(result)):
        print("YES")
    else:
        print("NO")
