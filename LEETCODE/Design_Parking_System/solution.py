class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.limit = [None, big, medium, small]
        self.parking = [None, 0, 0, 0]

    def addCar(self, carType: int) -> bool:

        if self.parking[carType] < self.limit[carType]:
            self.parking[carType] += 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
