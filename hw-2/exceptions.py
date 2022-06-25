def LowFuelError():
    raise Exception("refill fuel")

def NotEnoughFuel():
    raise Exception("Not enough fuel for that distance")

def CargoOverLoad():
    raise Exception("Cargo overloaded")

