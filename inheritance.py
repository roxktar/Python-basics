#SINGLE INHERITANCE 

class human:
    def __init__(self):
         self.num=3
         self.habit="walk"
    def show(self):
         print(f"HAND COUNTING IS {self.num} and habit is {self.habit}")
class male(human):
     def action(self):
         print("THIS IS INHERITANCE")

m1=male()
m1.show()


#MULTIPLE INHERITANce

class human:
    def __init__(self):
        super().__init__()
        print("hello")
        self.num=2
    def show(self):
        print(f"NO OF HANDS ARE {self.num}")
class animal:
    def __init__(self):
        print("hii")
        self.eye=5
    def order(self):
        print(f"ANIMAL HAS {self.eye}")

class combine(human,animal): 
    def __init__(self):
        super().__init__()
        print("bye")
    def char(self):
      print("THIS IS MULTIPLE INHERITANCE") 
c1=combine()
c1.show()
c1.order()
c1.char()


#MULTILEVEL INHERITANCE 

class car:
    def __init__(self):
        self.gear=5
        self.brake=1

    def start(self):
        print(f"CAR HAS {self.gear} AND CAR HAS {self.brake}")

class scooter(car):
    def __init__(self):
        self.handle=2
        super().__init__()
    def show(self):
        print("THIS IS SCOOTER ")

class bike(scooter):
    def design(self):
        print("THIS IS BIKE ")
b1=bike()
b1.show()
b1.start()
print(b1.handle)
b1.design()

### HEIARCHIAL INHERITANCE 

class animal:
    def __init__(self):
        print("THIS IS HEIARCHIAL INHERITANCE")
        self.num=3
    def show(self):
        print(f"THE NUMBER OF ANIMAL IS {self.num}")

class bird(animal):
    def __init__(self):
        super().__init__()
        print("second order")
        self.eye=2
        self.wings=2
    def fly(self):
        print("BIRD HAS {self.eye} AND {self.wings}")

b1=bird()
b1.show()
class insects(animal):
    def __init__(self):
        super().__init__()
        self.type="cockroach"
    def rub(self):
        print(f"INSECT IS {self.type}")

class reptiles(animal):
    def __init__(self):
        super().__init__()
        print("first order")
r1=reptiles()
r1.show()

