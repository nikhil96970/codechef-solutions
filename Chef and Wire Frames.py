# cook your dish here
T = int(input())

for tc in range(T):
    (n, m, x) = map(int, input().split(' '))
    
    output = x * (2*n + 2*m)
    
    print(output)
