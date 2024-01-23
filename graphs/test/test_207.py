import unittest

from graphs.n_207_course_schedule import CourseSchedule


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        num_courses = 2
        prerequisites = [[1, 0]]
        expected = True
        self.assertEqual(
            expected, CourseSchedule.solution(num_courses, prerequisites)
        )  # add assertion here

    def test_case_two(self):
        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = False
        self.assertEqual(expected, CourseSchedule.solution(num_courses, prerequisites))


if __name__ == "__main__":
    unittest.main()
