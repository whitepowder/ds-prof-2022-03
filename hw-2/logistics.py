import exceptions as ex


class BaseVehicle:

    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def insert_values(self, data):
        self.weight = data[0]
        self.started = data[1]
        self.fuel = data[2]
        self.fuel_consumption = data[3]

    def start(self, data):
        self.insert_values(data)
        if self.fuel < 1:
            print(ex.LowFuelError())
        elif self.started == 0:
            self.started = 1
            print('engine start')
        else:
            print('engine already started')

    def move(self, data):
        self.insert_values(data)
        distance = input('Enter distance to travel: \n')
        fuel_consumption_per_1_km = self.fuel_consumption / 100
        fuel_consumed = fuel_consumption_per_1_km * float(distance)
        if self.fuel - fuel_consumed < 0:
            print(ex.NotEnoughFuel())
        else:
            self.fuel = self.fuel - fuel_consumed
            print(f"remaining fuel is: {self.fuel} liters")


if __name__ == '__main__':
    car = BaseVehicle()
    # car.start([2000, 0, 0, 10])
    car.move([2000, 0, 10, 10])
