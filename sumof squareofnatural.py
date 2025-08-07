
def square(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum
a=square(int(input("enetr the number upto you want to calaculate :")))
print("the sum is ",a)