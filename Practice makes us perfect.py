# cook your dish here
a=list(map(int,input().split(' ')))
count=0
for i in a:
    if(i>=10):
        count+=1
print(count)
