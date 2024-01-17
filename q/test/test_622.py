import unittest

from q.n_622_design_circular_queue import DesignCircularQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        q = DesignCircularQueue(3)
        command = [
            "enQueue",
            "enQueue",
            "enQueue",
            "enQueue",
            "Rear",
            "isFull",
            "deQueue",
            "enQueue",
            "Rear",
        ]
        value = [[1], [2], [3], [4], [], [], [], [4], []]
        output = []
        for c, v in zip(command, value):
            q_command = getattr(q, c)
            output.append(q_command(*v))

        expected = [True, True, True, False, 3, True, True, True, 4]
        self.assertEqual(expected, output)  # add assertion here


if __name__ == "__main__":
    unittest.main()
