# cook 
F=int(input())
for q in range(F):
    a,x,b,y = map(int,input().split())
    ali = a/x
    bo = b/y
    if ali>bo:
        print("alice")
    elif ali<bo:
        print("bob")
    else:
        print ("equal")
    
