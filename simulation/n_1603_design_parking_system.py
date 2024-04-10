class ParkingLotBySize:
    def __init__(self, limit: int, number_of_cars_parking: int | None = 0):
        self.limit = limit
        self.number_of_cars_parking = number_of_cars_parking

    def is_parking_available(self):
        return self.limit > self.number_of_cars_parking

    def park(self):
        self.number_of_cars_parking += 1


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_parking_lot: ParkingLotBySize = ParkingLotBySize(limit=big)
        self.medium_parking_lot: ParkingLotBySize = ParkingLotBySize(limit=medium)
        self.small_parking_lot: ParkingLotBySize = ParkingLotBySize(limit=small)
        self.parking_lot_vector = {
            1: self.big_parking_lot,
            2: self.medium_parking_lot,
            3: self.small_parking_lot,
        }

    def add_car(self, car_type: int) -> bool:
        parking_lot: ParkingLotBySize = self.parking_lot_vector.get(car_type, None)
        if parking_lot is None or parking_lot.is_parking_available() is False:
            return False
        parking_lot.park()
        return True
