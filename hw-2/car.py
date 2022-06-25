import logistics
import engine


class Car(logistics.BaseVehicle):
    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None, car_engine=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = car_engine

    def set_engine(self):
        self.engine = engine.Engine
        print(f'Car engine volume is {self.engine.volume} and there are {self.engine.piston} pistons')


if __name__ == '__main__':
    car = Car()
    car.set_engine()
    car.start([2000, 0, 0, 10])
