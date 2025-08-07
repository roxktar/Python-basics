class Circel:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def Display(self):
         return 2*self.pi*self.r
    def Area(self):
        return self.r*self.r*self.pi
a=Circel(3)
print("The circumference is :",a.Display())
print("The area is :",a.Area()) 