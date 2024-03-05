#Car Class implementation

class Car:
    def __init__(self, company):
        self.company = company
    
    def start_engine(self):
        print("Vroom Vroom Vroom")

class ElectricCar(Car):
    def __init__(self,name):
        super().__init__("Tesla")
        self.name = name
    def start_engine(self):
        print("Hmmmm Hmmmm")


temp = Car("GMC")
electricCar = ElectricCar("Model S")

temp.start_engine()
electricCar.start_engine()

