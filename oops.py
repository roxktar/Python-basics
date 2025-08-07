class employee:
    organization="Microsoft"
    def __init__(self,name,address,salary):
        self.name=name
        self.address=address
        self.salary=salary
    def show(self):
        print(f"NAME IS {self.name} and ADDRESS IS {self.address}")
e1=employee("PUJA","DELHI",25000)


          