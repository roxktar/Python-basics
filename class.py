class employee:
    organization="microsoft"
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
print("Employee s1 details are :")
s1=employee('karan',12,10000)
print(s1.name)
print(s1.id)
print(s1.salary)
print("Employee s2 details are :")
s2=employee('ram',2,23000)
print(s1.name)
print(s1.id)
print(s1.salary)