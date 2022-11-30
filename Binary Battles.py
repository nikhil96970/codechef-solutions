import math

T = int(input())


def Binary():
    for i in range(0,T): 
        (N,A,B) = map(int,input().split())
        n = (math.log10(N) /math.log10(2))
        Y = ((A+B)*(n-1)+A)
        
        print(int(Y))
        
Binary()
           
