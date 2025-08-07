# POSITIONAL ARGUMENTS 

def Details(name,address):
    print("Name is :",name)
    print("ADD IS :",address)
Details("jenny", "delhi")

# KEYWORDS ARGUMENTS

def Details(name,dept):
    print("\nNAME IS :",name)
    print("DEPT  is :",dept)
Details(name="jenny",dept="cse")

#DEFAULT ARGUMENTS 


def Details(radius,circum,area=34):
    print("\nThe Radius is :",radius)
    print("The Circum is :",circum)
    print("The Area is :",area)
Details(4,22.5)


#ARBITARY ARGUMENTS 
  # 1.. POSITIONAL ARBITARY ARGUMENTS 

def sum(*number):
    c=0
    for i in number:
        c=c+i
    print("\nThe Sum is :",c)
sum(3,4,5,6,7)
sum(1,2,3,4,5,6,7,8,9)


  # 2..KEYWORDS ARBITARY ARGUMENTS 


