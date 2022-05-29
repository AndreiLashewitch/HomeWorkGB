class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск сортировки"

class Pen(Stationery):
    def draw(self):
        return f"Запус сортировки {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"Запус сортировки {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"Запус сортировки {self.title}"


pen = Pen("Ручек")
print(pen.draw())

pencil = Pencil("Карандашом")
print(pencil.draw())

handle = Handle("Маркером")
print(handle.draw())