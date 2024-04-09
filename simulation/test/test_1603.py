import unittest

from simulation.n_1603_design_parking_system import ParkingSystem


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        expected = [None, True, True, False, False]
        results = [None]
        parking_lot = ParkingSystem(1, 1, 0)
        results.append(parking_lot.add_car(1))
        results.append(parking_lot.add_car(2))
        results.append(parking_lot.add_car(3))
        results.append(parking_lot.add_car(1))
        self.assertEqual(expected, results)  # add assertion here


if __name__ == "__main__":
    unittest.main()
