import unittest

from programmers.hashtable.완주하지못한선수 import UncompletedPlayer


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        participant = ["leo", "kiki", "eden"]
        completion = ["eden", "kiki"]
        expected = "leo"
        self.assertEqual(
            expected, UncompletedPlayer.solution(participant, completion)
        )  # add assertion here

    def test_case_two(self):
        participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
        completion = ["josipa", "filipa", "marina", "nikola"]
        expected = "vinko"
        self.assertEqual(expected, UncompletedPlayer.solution(participant, completion))

    def test_case_three(self):
        participant = ["mislav", "stanko", "mislav", "ana"]
        completion = ["stanko", "ana", "mislav"]
        expected = "mislav"
        self.assertEqual(expected, UncompletedPlayer.solution(participant, completion))

    def test_case_four(self):
        participant = ["mislav", "stanko", "mislav", "ana"] * 25000
        completion = ["mislav", "stanko", "mislav", "ana"] * 24999 + [
            "mislav",
            "stanko",
            "mislav",
        ]
        expected = "ana"
        self.assertEqual(expected, UncompletedPlayer.solution(participant, completion))

    def test_case_five(self):
        participant = ["leo", "kiki", "eden"]
        completion = ["eden", "kiki"]
        expected = "leo"
        self.assertEqual(
            expected, UncompletedPlayer.solution_with_counter(participant, completion)
        )  # add assertion here

    def test_case_six(self):
        participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
        completion = ["josipa", "filipa", "marina", "nikola"]
        expected = "vinko"
        self.assertEqual(
            expected, UncompletedPlayer.solution_with_counter(participant, completion)
        )

    def test_case_seven(self):
        participant = ["mislav", "stanko", "mislav", "ana"]
        completion = ["stanko", "ana", "mislav"]
        expected = "mislav"
        self.assertEqual(
            expected, UncompletedPlayer.solution_with_counter(participant, completion)
        )

    def test_case_eight(self):
        participant = ["mislav", "stanko", "mislav", "ana"] * 25000
        completion = ["mislav", "stanko", "mislav", "ana"] * 24999 + [
            "mislav",
            "stanko",
            "mislav",
        ]
        expected = "ana"
        self.assertEqual(
            expected, UncompletedPlayer.solution_with_counter(participant, completion)
        )


if __name__ == "__main__":
    unittest.main()
