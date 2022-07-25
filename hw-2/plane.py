import logistics
import exceptions as ex


class Plane(logistics.BaseVehicle):
    def __init__(self, weight=None, started=None, fuel=None, fuel_consumption=None, cargo=None, max_cargo=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def insert_values(self, data):
        self.cargo = data[0]
        self.max_cargo = data[1]

    def load_cargo(self, data):
        self.insert_values(data)
        cargo_to_add = int(input('Enter weight of cargo to add: \n'))
        if cargo_to_add + self.cargo > self.max_cargo:
            print(ex.CargoOverLoad())
        else:
            self.cargo = cargo_to_add + self.cargo
            print(f'Current cargo weight is {self.cargo}')

    def remove_all_cargo(self):
        print(f'Last recorded cargo weight is {self.cargo}')
        self.cargo = 0
        print(f'Cargo has been reset, cargo weight is {self.cargo}')


if __name__ == '__main__':
    plane = Plane()
    plane.load_cargo([10, 200])
    plane.remove_all_cargo()

