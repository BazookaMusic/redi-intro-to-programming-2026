# 01 · Git and GitHub solutions

Try the [exercises](../../exercises/01-git-and-github/README.md) first, then check your work here.

## 1. Create and publish your repository

Your repository appears on GitHub.com under your account, and its folder is open in VS Code.

## 2. Create a file in your repository

`my-file.py` appears in the VS Code Explorer, inside your repository folder. It contains:

```python
print("hello")
```

## 3. Make and publish a commit

After `git push`, your repository page on GitHub shows the commit message `Update my file`. Open `my-file.py` on GitHub to see your new line.

## 4. Read this folder structure

1. **Files:** `hello.py`, `notes.txt`, `logo.png`
2. **Folders:** `my-project` and `images`
3. **File extension:** `.py`
4. **Path:** `my-project/images/logo.png`

## 5. Clone and play a Python game

`git status` shows that you are on a branch and that there is nothing to commit. The Bagels game starts and asks you to guess a three-digit number.

## 6. Build folders using commands (advanced)

Run one command at a time:

```sh
cd "$HOME"
mkdir terminal-practice
cd terminal-practice
mkdir notes
mkdir projects
ls
cd projects
mkdir python
ls
cd ..
ls
```

The final output should include `notes` and `projects`.
