import math
for _ in range(int(input())):
    h,x,y,c=list(map(int, input().split()))
    v=h*(x+math.floor(y/2))
    if(v<=c):
        print("yes")
    else:
        print("no")
