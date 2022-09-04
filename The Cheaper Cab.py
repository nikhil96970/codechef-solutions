for i in range(int(input())):
    a,b=map(int,input().split(' '))
    if b>a:
        print("FIRST")
    elif a>b:
        print("SECOND")
    else:
        print("ANY")
    
