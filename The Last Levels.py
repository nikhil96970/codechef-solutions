# cook your dish here
import math
for _ in range(int(input())):
    a,b,c=map(int,input().split(' '))
    if(a<=3):
        print(b*a)
    else:
        print((a*b)+((math.ceil(a/3))*c)-c)
