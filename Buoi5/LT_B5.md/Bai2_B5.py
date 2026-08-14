class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Phương tiện là {self.brand}, tốc độ {self.speed} km/h")


class Car(Vehicle):

    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def move(self):
        print(f"Ô tô {self.brand} đang chạy trên đường với tốc độ {self.speed} km/h")


class Boat(Vehicle):

    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def move(self):
        print(f"Thuyền {self.brand} đang di chuyển với tốc độ {self.speed} km/h")

car1 = Car("Porsche", 100)
car1.move()

boat1 = Boat("Titanic", -199)
boat1.move()
