import unittest
from unittest.mock import patch
from GraderClass import Grader


class TestGrader(unittest.TestCase):

    def check_grade(self, grade, expected_letter):
        """Run Grader and verify the expected letter grade."""
        with patch("builtins.input", side_effect=[
            "Heather",
            "Python Testing",
            str(grade)
        ]), patch("builtins.print") as mock_print:

            grader = Grader()
            result = grader.gradeInfo()

        output = mock_print.call_args[0][0]

        self.assertIn(expected_letter, output)
        self.assertIsNone(result)

        actual = expected_letter

        print(
            f"Grade: {grade} | "
            f"Expected: {expected_letter} | "
            f"Actual: {actual} | "
            f"PASS"
        )


    def check_returned_grade(self, grade):
        """Run Grader and verify that the numeric grade is returned."""
        with patch("builtins.input", side_effect=[
            "Heather",
            "Python Testing",
            str(grade)
        ]):

            grader = Grader()
            result = grader.gradeInfo()

        self.assertEqual(result, float(grade))
        self.assertIsInstance(result, float)

        print(
            f"Grade: {grade} | "
            f"Expected: {float(grade)} | "
            f"Actual: {result} | "
            f"PASS"
        )


    def check_invalid_grade(self, grade):
        """Run Grader and verify that an invalid grade returns an error."""
        with patch("builtins.input", side_effect=[
            "Heather",
            "Python Testing",
            str(grade)
        ]):

            grader = Grader()
            result = grader.gradeInfo()

        self.assertIsInstance(result, str)
        self.assertIn("grade number", result)

        print(
            f"Grade: {grade} | "
            f"Expected: Invalid grade | "
            f"Actual: Invalid grade | "
            f"PASS"
        )


    # Letter grade tests

    def test_grade_100(self):
        self.check_grade(100, "A")


    def test_grade_90(self):
        self.check_grade(90, "A")


    def test_grade_89(self):
        self.check_grade(89, "B")

    def test_grade_89_5(self):
        self.check_grade(89.5, "B")


    def test_grade_80(self):
        self.check_grade(80, "B")


    def test_grade_79(self):
        self.check_grade(79, "C")


    def test_grade_70(self):
        self.check_grade(70, "C")


    def test_grade_69(self):
        self.check_grade(69, "D")


    def test_grade_60(self):
        self.check_grade(60, "D")


    # Numeric return tests

    def test_grade_59(self):
        self.check_returned_grade(59)


    def test_grade_0(self):
        self.check_returned_grade(0)


    # Invalid grade tests

    def test_grade_negative_1(self):
        self.check_invalid_grade(-1)


    def test_grade_101(self):
        self.check_invalid_grade(101)


    def test_non_numeric_grade(self):
        with patch("builtins.input", side_effect=[
            "Heather",
            "Python Testing",
            "banana"
        ]):

            grader = Grader()
            result = grader.gradeInfo()

        self.assertIsInstance(result, str)
        self.assertIn("grade number", result)

        print(
            "Grade: banana | "
            "Expected: Invalid grade | "
            "Actual: Invalid grade | "
            "PASS"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)