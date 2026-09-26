from pathlib import Path
from shutil import copyfile
from tempfile import TemporaryDirectory
import subprocess
import sys
import unittest


LESSON = Path(__file__).parent
SOLUTIONS = LESSON.parents[1] / "solutions" / LESSON.name

SOURCES = {
    "about-me": """name = "Mina"
age = 31
city = "Oslo"
language = "Spanish"
is_student = False
print(name)
print(age)
print(city)
print(language)
print(is_student)
print(type(name))
print(type(age))
print(type(city))
print(type(language))
print(type(is_student))
age = age + 1
print(age)
print(len(name))
""",
    "type-detective": """print(type("42"))
print(int(3.9))
print(len("ReDI"))
# Text cannot be added to a number without conversion.
print("TypeError")
print(str(True))
print(type(3.0))
""",
    "homework-01-all-about-me": """name = "Mina"
age = 31
city = "Oslo"
favourite_food = "Sushi"
favourite_colour = "Green"
is_working = True
print(name)
print(age)
print(city)
print(favourite_food)
print(favourite_colour)
print(is_working)
""",
    "homework-02-type-inspector": """name = "Mina"
age = 31
city = "Oslo"
favourite_food = "Sushi"
favourite_colour = "Green"
is_working = True
print(type(name))
print(type(age))
print(type(city))
print(type(favourite_food))
print(type(favourite_colour))
print(type(is_working))
""",
    "homework-03-receipt": """item = "Tea"
price = 2.75
quantity = 3
print(item, "— quantity:", quantity, "— price:", price)
""",
    "homework-04-length-explorer": """name = "Alexander"
city = "Oslo"
food = "Rice"
print("Name length:", len(name))
print("City length:", len(city))
print("Food length:", len(food))
print("Longest:", name)
""",
    "homework-05-mad-libs": """adjective = "brave"
animal = "dog"
place = "Paris"
number = 2
print("The " + adjective + " " + animal + " visited " + str(number) + " places in " + place + ".")
""",
    "homework-06-converter-chain": """age_text = "28"
age_text = int(age_text)
print(type(age_text))
age_text = float(age_text)
print(type(age_text))
age_text = str(age_text)
print(type(age_text))
""",
    "homework-07-interactive-profile": """name = input("Your name: ")
age = input("Your age: ")
print("Hello, " + name + "! You are " + age + " years old.")
print("Name length:", len(name))
""",
    "bonus-swap-variables": """first = 5
second = 9
temporary = first
first = second
second = temporary
print("First:", first)
print("Second:", second)
""",
}


class CheckingTests(unittest.TestCase):
    def run_pair(self, name, source):
        with TemporaryDirectory() as folder:
            location = Path(folder)
            copyfile(LESSON / name / "check.py", location / "check.py")
            (location / "exercise.py").write_text(source, encoding="utf-8")
            return subprocess.run(
                [sys.executable, "check.py"],
                cwd=location,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )

    def test_every_task_has_a_standalone_pair(self):
        folders = {path.parent.name for path in LESSON.glob("*/exercise.py")}
        self.assertEqual(folders, set(SOURCES))
        for name in SOURCES:
            with self.subTest(folder=name):
                self.assertTrue((LESSON / name / "check.py").is_file())
                result = self.run_pair(name, "# Write your solution below.\n")
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertIn("Expected output", result.stdout)
                self.assertIn("Your output:\n(nothing)", result.stdout)

    def test_each_checker_accepts_a_correct_answer_with_chosen_values(self):
        for name, source in SOURCES.items():
            with self.subTest(folder=name):
                result = self.run_pair(name, source)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("Correct!", result.stdout)
                self.assertEqual(result.stderr, "")

    def test_every_solution_passes_its_matching_checker(self):
        solutions = list(SOLUTIONS.glob("*/exercise.py"))
        self.assertEqual({path.parent.name for path in solutions}, set(SOURCES))
        self.assertFalse(list(SOLUTIONS.glob("*/check.py")))
        for name in SOURCES:
            with self.subTest(folder=name):
                source = (SOLUTIONS / name / "exercise.py").read_text(encoding="utf-8")
                result = self.run_pair(name, source)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("Correct!", result.stdout)
                self.assertEqual(result.stderr, "")

    def test_personal_output_must_match_the_variables(self):
        source = SOURCES["homework-01-all-about-me"].replace("print(name)", 'print("Sara")')
        result = self.run_pair("homework-01-all-about-me", source)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected output:\nMina", result.stdout)
        self.assertIn("Your output:\nSara", result.stdout)

    def test_interactive_profile_bonus_is_optional(self):
        source = SOURCES["homework-07-interactive-profile"].replace(
            'print("Name length:", len(name))\n', ""
        )
        result = self.run_pair("homework-07-interactive-profile", source)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_interactive_profile_rejects_a_hardcoded_answer(self):
        source = (
            'input("Name: ")\ninput("Age: ")\n'
            'print("Hello, Sara! You are 25 years old.")\n'
        )
        result = self.run_pair("homework-07-interactive-profile", source)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected output", result.stdout)
        self.assertIn("Your output", result.stdout)

    def test_length_explorer_needs_one_longest_word(self):
        source = SOURCES["homework-04-length-explorer"].replace(
            'name = "Alexander"', 'name = "Ada"'
        ).replace('city = "Oslo"', 'city = "Rio"').replace('food = "Rice"', 'food = "Pie"')
        result = self.run_pair("homework-04-length-explorer", source)
        self.assertEqual(result.returncode, 1)
        self.assertIn("one clear longest word", result.stdout)

    def test_bonus_rejects_unswapped_values(self):
        source = (
            'first = 5\nsecond = 9\nprint("First:", first)\nprint("Second:", second)\n'
        )
        result = self.run_pair("bonus-swap-variables", source)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Expected output:\nFirst: 9\nSecond: 5", result.stdout)
        self.assertIn("Your output:\nFirst: 5\nSecond: 9", result.stdout)


if __name__ == "__main__":
    unittest.main()
