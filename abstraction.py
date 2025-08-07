from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self):
        self.no_of_cars=3

    @abstractmethod
    def show(self):
        pass



        
