for _ in range(int(input())):
    x,y=map(int,input().split(" "))
    if x>=y:
        if x%y==0:
            print(int(x/y))
        else:
            a=int(x/y)
            b=(x-(a*y))
            print(a+b)
    else:
        print(x)
            
        
