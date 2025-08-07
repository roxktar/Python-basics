class encapsulation:
    def __init__(self,name,age):
        self.name=name
        self.__age=age # private variable

    def get_age(self):
        return self.__age
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age must be positive")
obj=encapsulation("John",25)
print(obj.get_age()) # Accessing private variable using getter method
obj.set_age(20) # Accessing private variable using setter method
print(obj.get_age()) # Accessing private variable using getter method
print(obj.name) # Accessing public variable directly