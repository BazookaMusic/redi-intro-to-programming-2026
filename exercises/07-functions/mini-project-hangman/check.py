import ast
import contextlib
import io
from pathlib import Path
import random
import runpy
import sys
import types
from unittest.mock import patch


def main():
    path = Path(__file__).with_name("exercise.py")
    library = types.ModuleType("english_words")

    def word_set(sources, lower=False):
        assert sources == ["web2"] and lower, "Use ['web2'] with lower=True."
        return {"linguist", "elephant", "apple", "cat", "bad-word", "caféxxxx"}

    library.get_english_words_set = word_set
    try:
        tree = ast.parse(path.read_text())
        definitions = ast.Module(body=[
            node for node in tree.body
            if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef))
        ], type_ignores=[])
        code = {}
        with patch.dict(sys.modules, {"english_words": library}):
            exec(compile(definitions, str(path), "exec"), code)
        function = code.get("get_random_secret_word")
        assert callable(function), "Write get_random_secret_word(length)."
        for length, expected in [(8, {"linguist", "elephant"}), (5, {"apple"}), (3, {"cat"})]:
            for selected in expected:
                def choose(words):
                    assert set(words) == expected, (
                        f"Expected {length}-letter choices: {expected!r}\nActual: {words!r}"
                    )
                    return selected
                with patch.object(random, "choice", choose):
                    actual = function(length)
                assert actual == selected, f"Expected: {selected!r}\nActual: {actual!r}"
        for name, cases in [
            ("display_hidden_word", [
                (("linguist", []), "________"),
                (("linguist", ["i"]), "_i___i__"),
                (("linguist", list("lingust")), "linguist"),
                (("banana", ["a", "z"]), "_a_a_a"),
            ]),
            ("victory", [
                (("_i___i__",), False),
                (("linguist",), True),
                (("________",), False),
            ]),
        ]:
            function = code.get(name)
            assert callable(function), f"Write {name}."
            for args, expected in cases:
                actual = function(*args)
                assert actual == expected and type(actual) is type(expected), (
                    f"{name}{args!r}\nExpected: {expected!r}\nActual: {actual!r}"
                )

        function = code.get("get_user_guess")
        assert callable(function), "Write get_user_guess(guessed_letters)."
        for inputs, guesses, expected in [
            ([" A "], [], "a"),
            (["", "ab", "1", "é", "i", "Z"], ["i"], "z"),
        ]:
            answers = iter(inputs)
            output = io.StringIO()
            with patch("builtins.input", lambda prompt: next(answers)), \
                    contextlib.redirect_stdout(output):
                actual = function(guesses)
            assert actual == expected, f"Expected guess: {expected!r}\nActual: {actual!r}"
            if len(inputs) > 1:
                assert output.getvalue().strip(), "Explain why invalid guesses are rejected."

        def play(inputs):
            output = io.StringIO()
            answers = iter(inputs)
            def read(prompt):
                try:
                    return next(answers)
                except StopIteration:
                    raise AssertionError("The game asked for extra guesses. Check victory and the loop.")
            def choose(words):
                assert set(words) == {"linguist", "elephant"}, (
                    f"Expected eight-letter English words.\nActual: {words!r}"
                )
                return "linguist"
            with patch.dict(sys.modules, {"english_words": library}), \
                    patch.object(random, "choice", choose), \
                    patch("builtins.input", read), contextlib.redirect_stdout(output):
                runpy.run_path(str(path), run_name="__main__")
            return output.getvalue()

        actual = play(["", "ab", "1", " I ", "i", "l", "n", "g", "u", "s", "t"])
        for expected in ["________", "_i___i__", "linguist", "You won!"]:
            assert expected in actual, f"Expected output to contain: {expected!r}\nActual:\n{actual}"
        assert "Wrong guess!" not in actual, f"Invalid or repeated guesses used a life:\n{actual}"
        actual = play(["z", "x", "q", "v", "j", "k"])
        assert actual.count("Wrong guess!") == 6, f"Expected six mistakes.\nActual:\n{actual}"
        assert "You lost 💀 The word was linguist." in actual, f"Expected a loss and the secret word.\nActual:\n{actual}"
        assert "You won!" not in actual, f"Expected a loss.\nActual:\n{actual}"
        actual_loss_output = actual
        bar = code.get("lives_bar")
        assert callable(bar), "Keep the supplied lives_bar function."
        for total in [6, 3]:
            for left in range(total + 1):
                expected = "_" * (total - left) + "💀" + "_" * left + "😊"
                actual = bar(total, left)
                assert actual == expected, (
                    f"lives_bar({total}, {left})\nExpected: {expected!r}\nActual: {actual!r}"
                )
        for left in range(7):
            expected = bar(6, left)
            assert expected in actual_loss_output, (
                f"Expected the supplied lives bar each turn.\nExpected: {expected!r}"
            )
        print("PASS all three functions and the game.")
    except Exception as error:
        print(f"Not yet: {type(error).__name__}: {error}")
        raise SystemExit(1)


main()
