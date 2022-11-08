for i in range(int(input())):
    a,b=map(int,input().split())
    a*=2
    b*=5
    if(a>b):
        print("Chocolate")
    elif(a<b):
        print("Candy")
    else:
        print("Either")
