from math import isclose
from pathlib import Path
from shutil import copyfile
from tempfile import TemporaryDirectory
import re
import runpy
import subprocess
import sys
import unittest


LESSON = Path(__file__).parent


class CheckingTests(unittest.TestCase):
    def run_copied_checker(self, checker, source):
        with TemporaryDirectory() as folder:
            copied = Path(folder)
            copyfile(checker, copied / "check.py")
            copyfile(checker.with_name("exercise.py"), copied / "exercise.py")
            (copied / "exercise.py").write_text(source, encoding="utf-8")
            return subprocess.run(
                [sys.executable, "check.py"],
                cwd=copied,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )

    def test_every_checker_runs_with_only_two_files(self):
        checkers = sorted(LESSON.glob("*/check.py"))
        self.assertEqual(len(checkers), 8)
        for checker in checkers:
            with self.subTest(folder=checker.parent.name):
                result = self.run_copied_checker(checker, "# Write your solution below.\n")
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertIn("Not quite yet.", result.stdout)
                self.assertIn("Expected output:", result.stdout)
                self.assertIn("Your output:\n(nothing)", result.stdout)

    def test_copied_checker_simulates_input_and_accepts_a_solution(self):
        checker = LESSON / "homework-06-seconds-converter" / "check.py"
        source = (
            "seconds = int(input('Seconds: '))\n"
            "print('Minutes:', seconds // 60)\n"
            "print('Seconds:', seconds % 60)\n"
        )
        result = self.run_copied_checker(checker, source)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Correct! Your output matches every test.", result.stdout)

    def test_copied_checker_shows_expected_and_actual_output(self):
        checker = LESSON / "homework-06-seconds-converter" / "check.py"
        source = (
            "seconds = int(input('Seconds: '))\n"
            "print('Minutes:', seconds)\n"
            "print('Seconds:', seconds)\n"
        )
        result = self.run_copied_checker(checker, source)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected output:\nMinutes: 2\nSeconds: 5", result.stdout)
        self.assertIn("Your output:\nMinutes: 125\nSeconds: 125", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_copied_checker_requires_the_right_number_of_inputs(self):
        checker = LESSON / "homework-06-seconds-converter" / "check.py"
        for source, message in (
            ("print('Minutes: 2')\nprint('Seconds: 5')\n", "asked for 0 input(s)"),
            ("input('First: ')\ninput('Second: ')\n", "asked for more than 1 input(s)"),
        ):
            with self.subTest(source=source):
                result = self.run_copied_checker(checker, source)
                self.assertEqual(result.returncode, 1)
                self.assertIn(message, result.stdout)
                self.assertEqual(result.stderr, "")

    def test_each_checker_preserves_numeric_and_label_comparisons(self):
        for checker in sorted(LESSON.glob("*/check.py")):
            with self.subTest(folder=checker.parent.name):
                matches = runpy.run_path(str(checker))["_matches"]
                self.assertTrue(matches("Total: 3", "total: 3.0"))
                self.assertFalse(matches("Total: 3", "Wrong: 3"))
                self.assertFalse(matches("Total: 3", "Total: 3.001"))

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

    def test_each_starter_example_matches_its_first_check(self):
        checkers = sorted(LESSON.glob("*/check.py"))
        self.assertEqual(len(checkers), 8)
        for checker in checkers:
            with self.subTest(folder=checker.parent.name):
                comments = checker.with_name("exercise.py").read_text(encoding="utf-8").splitlines()
                self.assertIn("# Example output:", comments)
                start = comments.index("# Example output:") + 1
                example = []
                for line in comments[start:]:
                    if not line.startswith("# "):
                        break
                    example.append(line[2:])

                answers, expected = runpy.run_path(str(checker))["CASES"][0]
                self.assertEqual(len(example), len(expected))
                for shown, wanted in zip(example, expected):
                    shown_label, _, shown_number = shown.partition(":")
                    wanted_label, _, wanted_number = wanted.partition(":")
                    self.assertEqual(shown_label, wanted_label)
                    self.assertTrue(
                        isclose(float(shown_number), float(wanted_number), rel_tol=0, abs_tol=1e-9)
                    )

                if answers:
                    input_lines = [line for line in comments if line.startswith("# Example input:")]
                    self.assertEqual(len(input_lines), 1)
                    self.assertEqual(
                        tuple(re.findall(r"-?\d+(?:\.\d+)?", input_lines[0])), answers
                    )


if __name__ == "__main__":
    unittest.main()
