for i in range(int(input())):
    x,y,x1,y1,D = map(int,input().split())
    food = x/x1
    water = y/y1
    days = min(food,water)
    if days >= D:
        print("YES")
    else:
        print("NO")
