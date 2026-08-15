class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = vehicle(240, 18)
print(f"ModelX has a max speed of {modelX.max_speed} km/h and mileage of {modelX.mileage}.")