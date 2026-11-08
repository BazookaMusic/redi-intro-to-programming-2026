import contextlib
import io
from pathlib import Path
import random
import runpy
from unittest.mock import patch


def main():
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            code = runpy.run_path(str(Path(__file__).with_name("exercise.py")))
        function = code.get("game_words")
        assert callable(function), "Write game_words(words)."
        for words, expected in [
            (["cat", "apple", "banana", "watermelon"], ["apple", "banana"]),
            (["a", "cat", "pear", "elephant", "pineapple"], ["pear", "elephant"]),
            ([], []),
            (["pear", "pear"], ["pear", "pear"]),
        ]:
            actual = function(words)
            assert actual == expected, f"Expected: {expected!r}\nActual:   {actual!r}"
        actual = output.getvalue().strip()
        expected = "['apple', 'banana']"
        assert actual == expected, f"Expected printed output: {expected}\nActual: {actual!r}"
        advanced = code.get("pick_word")
        if advanced is None:
            print("PASS required steps. Advanced pick_word is missing.")
        else:
            assert callable(advanced), "pick_word must be a function."
            for selected in ["apple", "banana"]:
                def choose(options):
                    assert list(options) == ["apple", "banana"], (
                        f"Expected random.choice options: ['apple', 'banana']\nActual: {options!r}"
                    )
                    return selected
                with patch.object(random, "choice", choose):
                    actual = advanced(["cat", "apple", "banana", "watermelon"])
                assert actual == selected, f"Expected: {selected!r}\nActual: {actual!r}"
            print("PASS required and advanced steps.")
    except Exception as error:
        print(f"Not yet: {type(error).__name__}: {error}")
        raise SystemExit(1)


main()
