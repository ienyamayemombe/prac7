from turtle import speed


class Car:
    def __init__(self,topSpeed):
        self.setTopSpeed(topSpeed)
        self.__speed=speed
        print('Car',self.__topSpeed,self.__speed)

    def setTopSpeed(self,topSpeed):
        if topSpeed >0:
            self.__topSpeed=topSpeed
        else:
            pass #fix code


car=Car(220)