class Space:
    def __init__(self, name, speed, fuel, cargo):
        self.name = name
        self.fuel = fuel if 0 <= fuel <= 100 else 50
        self.speed = speed if 1 <= speed <= 10 else 1
        self.cargo = cargo if 0 <= cargo <= 50 else 0

    def fly(self):
        return f"{self.name} is flying at speed {self.speed}!"

    def refuel(self, refurel):
        self.fuel += refurel
        if self.fuel > 100:
            self.fuel = 100
        return f"{self.name} refueled to {self.fuel} units!"

    def upgrade_speed(self):
        self.speed += 1
        if self.speed > 10:
            self.speed = 10
        return f"{self.name} upgraded to speed {self.speed}!"

    def load_cargo(self, amount):
        self.cargo += amount
        if self.cargo > 50:
            self.cargo = 50
        return f"{self.name} loaded {self.cargo} units of cargo!"

    def unload_cargo(self, amount):
        self.cargo -= amount
        if self.cargo < 0:
            self.cargo = 0
        return f"{self.name} unloaded to {self.cargo} units of cargo!"


ship = Space("SpaceX", 20, 40, 25)
print(ship.fly())
print(ship.refuel(10))
print(ship.upgrade_speed())
print(ship.load_cargo(10))
print(ship.unload_cargo(5))