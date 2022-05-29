from time import sleep

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]
    def __running (self, __color):
        i = 0
        for i in __color:
            print(TrafficLight.__color)
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)

t = TrafficLight
t._TrafficLight.__running(self, __color)
print(t._TrafficLight__color)

