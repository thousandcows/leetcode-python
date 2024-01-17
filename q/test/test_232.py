import unittest

from q.n_232_implement_queue_using_stacks import ImplementQueueUsingStacks


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        q = ImplementQueueUsingStacks()
        commands = ["push", "push", "peek", "pop", "empty"]
        args = [[1], [2], [], [], []]
        result = []
        for c, a in zip(commands, args):
            q_method = getattr(q, c)
            result.append(q_method(*a))

        self.assertEqual([None, None, 1, 1, False], result)

    def test_case_two(self):
        q = ImplementQueueUsingStacks()
        commands = ["push", "push", "push", "pop", "peek", "empty"]
        args = [[1], [2], [3], [], [], []]
        result = []
        for c, a in zip(commands, args):
            q_method = getattr(q, c)
            result.append(q_method(*a))

        self.assertEqual([None, None, None, 1, 2, False], result)

    def test_case_three(self):
        q = ImplementQueueUsingStacks()
        commands = [
            "empty",
            "push",
            "push",
            "push",
            "pop",
            "pop",
            "pop",
            "pop",
            "empty",
        ]
        args = [[], [1], [2], [3], [], [], [], [], []]
        result = []
        for c, a in zip(commands, args):
            q_method = getattr(q, c)
            result.append(q_method(*a))

        self.assertEqual([True, None, None, None, 1, 2, 3, -1, True], result)


if __name__ == "__main__":
    unittest.main()
