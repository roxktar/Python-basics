#factorial
def fact(n):
 f=1
 for i in range(1,n+1):
      f=f*i
 return f
factorial=fact(int(input('enter the number :')))
print(factorial)