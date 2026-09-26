from contextlib import redirect_stdout
from io import StringIO
from math import isclose
from pathlib import Path
from tempfile import TemporaryDirectory
import runpy
import unittest

from checking import check_output, run_check


LESSON = Path(__file__).parent


class CheckingTests(unittest.TestCase):
    def run_source(self, source, cases):
        with TemporaryDirectory() as folder:
            exercise = Path(folder) / "exercise.py"
            exercise.write_text(source, encoding="utf-8")
            result = StringIO()
            with redirect_stdout(result):
                check_output(exercise, cases)
            return result.getvalue()

    def test_simulates_input_and_accepts_equivalent_numeric_output(self):
        source = "number = float(input('Number: '))\nprint('Double: ', number * 2)\n"
        cases = (
            (("2",), ("Double: 4",)),
            (("2.5",), ("Double: 5.0",)),
        )
        self.assertIn("Correct!", self.run_source(source, cases))

    def test_wrong_answer_shows_expected_and_actual_output(self):
        source = "number = float(input('Number: '))\nprint('Double:', number * 3)\n"
        with self.assertRaises(AssertionError) as failure:
            self.run_source(source, ((("2",), ("Double: 4",)),))
        self.assertIn("Expected output:\nDouble: 4", str(failure.exception))
        self.assertIn("Your output:\nDouble: 6.0", str(failure.exception))

    def test_missing_input_fails_even_if_output_matches(self):
        with self.assertRaises(AssertionError) as failure:
            self.run_source("print('Double: 4')\n", ((("2",), ("Double: 4",)),))
        self.assertIn("asked for 0 input(s)", str(failure.exception))

    def test_extra_input_has_a_clear_error(self):
        source = "input('First: ')\ninput('Second: ')\n"
        with self.assertRaises(AssertionError) as failure:
            self.run_source(source, ((("2",), ("Double: 4",)),))
        self.assertIn("asked for more than 1 input(s)", str(failure.exception))
        self.assertIn("Your output:\n(nothing)", str(failure.exception))

    def test_wrong_label_and_unrounded_answer_fail(self):
        for source in ("print('Triple: 4')\n", "print('Double: 4.001')\n"):
            with self.subTest(source=source), self.assertRaises(AssertionError):
                self.run_source(source, (((), ("Double: 4",)),))

    def test_all_starter_files_fail_with_helpful_messages(self):
        checkers = sorted(LESSON.glob("*/check.py"))
        self.assertEqual(len(checkers), 8)
        for checker in checkers:
            with self.subTest(folder=checker.parent.name):
                cases = runpy.run_path(str(checker))["CASES"]
                with self.assertRaises(AssertionError) as failure:
                    check_output(checker.with_name("exercise.py"), cases)
                self.assertIn("Expected output:", str(failure.exception))
                self.assertIn("Your output:\n(nothing)", str(failure.exception))

    def test_command_shows_feedback_without_a_traceback(self):
        output = StringIO()
        exercise = LESSON / "homework-02-average" / "exercise.py"
        with redirect_stdout(output), self.assertRaises(SystemExit) as failure:
            run_check(exercise, (((), ("Average: 81.7",)),))
        self.assertEqual(failure.exception.code, 1)
        self.assertIn("Not quite yet.", output.getvalue())
        self.assertIn("Expected output:\nAverage: 81.7", output.getvalue())
        self.assertIn("Your output:\n(nothing)", output.getvalue())
        self.assertNotIn("Traceback", output.getvalue())

    def test_all_expected_answers_match_the_math(self):
        def calculator(answers):
            a, b = map(float, answers)
            return (a + b, a - b, a * b, round(a / b, 2), a % b, a ** b)

        def operators(_):
            a, b = 17, 5
            return (a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

        def extended(answers):
            a, b = map(float, answers)
            return (*calculator(answers), a // b)

        expected_values = {
            "mini-project-calculator": calculator,
            "homework-01-all-operators": operators,
            "homework-02-average": lambda _: (round((70 + 85 + 90) / 3, 1),),
            "homework-03-temperature-difference": lambda _: (abs(-3 - 9),),
            "homework-04-discount-calculator": lambda a: (
                round(float(a[0]) * (1 - float(a[1]) / 100), 2),
            ),
            "homework-05-bmi-calculator": lambda a: (
                round(float(a[0]) / float(a[1]) ** 2, 1),
            ),
            "homework-06-seconds-converter": lambda a: (
                int(a[0]) // 60, int(a[0]) % 60
            ),
            "homework-07-extended-calculator": extended,
        }
        for folder, calculate in expected_values.items():
            cases = runpy.run_path(str(LESSON / folder / "check.py"))["CASES"]
            for answers, output in cases:
                with self.subTest(folder=folder, answers=answers):
                    values = calculate(answers)
                    self.assertEqual(len(output), len(values))
                    for line, value in zip(output, values):
                        self.assertTrue(
                            isclose(float(line.partition(":")[2]), value, rel_tol=0, abs_tol=1e-9),
                            line,
                        )


if __name__ == "__main__":
    unittest.main()
