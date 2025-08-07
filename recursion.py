#WAP FACTORIAL OF A NUMBER 

def fact(n):
    if(n==0 or n==1):
     return 1 
    else:
        
        return n*fact(n-1) 
a=fact(int(input("enter the number :")))
print(a)

#print the number from 20 to 1 using RECURSION
def reverse(n):
    if(n==0): 
        return 1
    else: 
        print(n)
        reverse(n-1)
a=reverse(int(input('enetr the number :')))   
  
#recursion
# Write a Python program to calculate the sum of a list of numbers using recursion.


def sum_list(n): 
    if(len(n)==0):
        return 0
    else:
        return n[0]+sum_list(n[1:])

a=sum_list([1,2,3,4,5])
print(a)    