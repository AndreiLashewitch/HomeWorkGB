class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"The{self.name} went."

    def stop(self):
        return f"\n The{self.name} stopped"

    def turn(self, direction):
        return f"\n The {self.name} turned {direction}"

    def show_speed(self):
        return f"\n The {self.name} has speed {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Your speed more on {(int(self.speed) - 60)}")
        else:
            return f"Speed {self.name} is normal"

class SportCar(Car):
    pass

class Work(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Your speed more on {(int(self.speed) - 40)}")
        else:
            return f"Speed {self.name} is normal"


class PoliceCar(Car):
    pass


town = TownCar(60, "red", "Audi", False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar(80, "Blue", "Porsche", False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('up'), sport.turn('right'), sport.stop())
