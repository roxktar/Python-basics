num=int(input('enter the number of terms :'))
a=0
b=1
c=a+b
print(a,end=",")
print(b,end=",")
for i in range(1,num+1):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c,end=",")