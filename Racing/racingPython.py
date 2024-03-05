import random
class Vehicle:
    def __init__(self, name, topSpeed, reliability): # reliability on a scale of 1 - 100, 100 = most, 1 = least
        self.name = name
        self.topSpeed = topSpeed
        self.reliability = reliability
    isCarBroke = False
    distanceCovered = 0
    def move(self):
        self.distanceCovered += self.topSpeed/5 
        print(f"{self.name} covers {self.distanceCovered}")

    def breakdown(self):
        chanceOfBreakdown = int(self.reliability / 10)
        randomNumber = random.randint(1, chanceOfBreakdown)
        if randomNumber == chanceOfBreakdown:
           print("Car has broken down")
           self.isCarBroke = True


class Car(Vehicle):
    def __init__(self, name, topSpeed, reliability, typeOfCar, driveMode):
        super().__init__(name, topSpeed, reliability)
        self.typeOfCar = typeOfCar
        self.driveMode = driveMode

    def start_engine(self):
        print("Vrooom Vroom Vroom")
        print(f"the {self.name} {self.typeOfCar }is ready to go in {self.driveMode}")
    
    def move(self):
        if self.driveMode == "RWD" and self.distanceCovered > 10:
            self.topSpeed += 100
        if self.driveMode == "4WD" and self.distanceCovered < 10:
            self.topSpeed += 10
        movement = self.topSpeed / 10
        self.distanceCovered += movement
        print(f"{self.name} moved {movement} feet, Total Covered: {self.distanceCovered} feet")


class Motorcycle(Vehicle):
    def __init__(self, name, topSpeed, reliability, numOfCC, weight):
        super().__init__(name, topSpeed, reliability)
        self.numOfCC = numOfCC
        self.weight = weight
    distanceCovered = 0
    def move(self):
        if self.numOfCC > 150:
            self.topSpeed += 5
        if self.weight >= 200:
            self.topSpeed -= 5
        movement = self.topSpeed / 10
        self.distanceCovered += movement
        print(f"{self.name} moved {movement} feet, Total Covered: {self.distanceCovered} feet")

class Truck(Vehicle):
    def __init__(self, name, topSpeed, reliability, numWheels, weight):
        super().__init__(name, topSpeed, reliability)
        self.numWheels = numWheels
        self.weight = weight
    distanceCovered = 0
    def move(self):
        if self.numWheels > 4 or self.weight >= 1000:
            self.topSpeed -= 5
        movement = self.topSpeed / 10
        self.distanceCovered += movement
        print(f"{self.name} moved {movement} feet, Total Covered: {self.distanceCovered} feet")




def race(vehicle1, vehicle2, distance):
    while vehicle1.distanceCovered < distance and vehicle2.distanceCovered < distance:
        if vehicle1.isCarBroke and vehicle2.isCarBroke:
            print("Both vehicles are broken race is over!")
            break

        whosTurn = random.randint(1,2)
        if whosTurn % 2 == 0 and vehicle1.isCarBroke != True:
            vehicle1.move()
            vehicle1.breakdown()
            if vehicle1.distanceCovered >= distance:
                print(f"{vehicle1.name} WINS!!")
        else: 
            if vehicle2.isCarBroke != True :
                vehicle2.move()
                vehicle2.breakdown()
                if vehicle2.distanceCovered >= distance:
                    print(f"{vehicle2.name} WINS!!")


gtr = Car("Nissan GTR", 200, 100, "Sport","RWD")
amg = Car("Mercedes AMG", 200, 100, "Sport", "4WD")
suzuki = Motorcycle("Suzki", 200, 100, 200, 100)
race(gtr,amg,500)