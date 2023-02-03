# cook your dish here
t = int(input())

for i in range(t):
    N, A, B = map(int, input().split())
    
    time = (6*60) + 2*N - A - B
    
    print(time)
