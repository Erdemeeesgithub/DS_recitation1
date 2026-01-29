class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
        
    def get_description(self):
        base = super().get_description()
        return f"{base}, {self.doors}-door"


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def get_description(self):
        base = super().get_description()
        return f"{base}, Payload capacity: {self.payload_capacity} tons"

# Do not change or remove the code below this point
def main():
    car = Car("Toyota", "Corolla", 2021, 4)
    print(car.get_description())  # Expected: "2021 Toyota Corolla, 4-door"

    truck = Truck("Ford", "F-150", 2020, 1.5)
    print(truck.get_description())  # Expected: "2020 Ford F-150, Payload capacity: 1.5 tons"


if __name__ == "__main__":
    main()
