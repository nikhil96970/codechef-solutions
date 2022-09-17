# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split(' '))
    m=a/(b**2)
    if(m<=18):
        print("1")
    elif(m<=24):
        print("2")
    elif(m<30):
        print("3")
    else:
        print("4")
