x=int(input())
while x!=0:
    y=int(input())
    if y<3:
        print('LIGHT')
    elif y>=3 and y<7:
        print('MODERATE')
    elif y>=7:
        print('HEAVY')
    x=x-1
