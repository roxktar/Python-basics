n1=int(input('enter the lower range '))
n2=int(input("enter the higher number "))
#sum of odd number in between two numbers 
sum=0
for i in range(n1,n2):
      if i%2==0:
        pass
      else:
         print(i,end=",")
         sum=sum+i

print("the sum is ",sum,end=" ")


#sum of even number in betwwen twio numbers 
n1=int(input('enter the lower range '))
n2=int(input("enter the higher number "))
sum=0
for i in range(n1,n2):
      if i%2==0:
         print(i,end=",")
         sum=sum+i

print("the sum is ",sum,end=" ")
 
