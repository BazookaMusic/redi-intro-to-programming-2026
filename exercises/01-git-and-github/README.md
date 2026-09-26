# 01 · Git and GitHub exercises

These exercises come from the [Git and GitHub slides](https://bazookamusic.github.io/redi-intro-to-programming-2026/slides_no_solutions/01-github-desktop.html). Do them in order. When you finish, compare your work with the [solutions](../../solutions/01-git-and-github/README.md).

You need GitHub Desktop, VS Code, and Git.

## 1. Create and publish your repository

1. In GitHub Desktop, choose **File → New Repository…**.
2. Name it, choose a folder, and add a README.
3. Click **Publish repository**.
4. Choose **Repository → Open in Visual Studio Code**.

**Done when:** your repository is online and open in VS Code.

## 2. Create a file in your repository

1. In the VS Code Explorer, click **New File**.
2. Type `my-file.py`, then press **Enter**.
3. Type `print("hello")`, then save with **Ctrl+S** (Windows) or **Command+S** (macOS).

**Done when:** `my-file.py` appears inside your repository folder.

## 3. Make and publish a commit

1. Open `my-file.py` and add a new line, for example:

   ```python
   print("I made a commit!")
   ```

2. Save the file with **Ctrl+S** (Windows) or **Command+S** (macOS).
3. In VS Code, choose **Terminal → New Terminal**.
4. Type these commands one line at a time. Press **Enter** after each line.

```sh
git status            # Check what changed
git add ./my-file.py  # Choose my-file.py for the commit
git status            # Check that my-file.py is green
git commit -m "Update my file" # Create the commit
git status            # Check that the commit is ready
git push              # Send it to GitHub
```

**Done when:** you open your repository on GitHub and see the new commit.

## 4. Read this folder structure

Study this tree:

```text
my-project/
|-- hello.py
|-- notes.txt
`-- images/
    `-- logo.png
```

Then answer these questions:

1. Name the **three files**.
2. Name the **two folders**.
3. What is the file extension of `hello.py`?
4. What path leads from `my-project` to `logo.png`?

## 5. Clone and play a Python game

1. In VS Code, choose **File → New Window**.
2. Choose **Terminal → New Terminal**. Run every command below in that terminal.
3. Copy the game repository to your computer:

   ```sh
   git clone https://github.com/asweigart/PythonStdioGames.git
   ```

4. Choose **File → Open Folder...** and open the new `PythonStdioGames` folder. Find `bagels.py`.
5. Open a new terminal in that window and run:

   ```sh
   git status
   ```

6. Run the game on Windows:

   ```powershell
   python src/gamesbyexample/bagels.py
   ```

   On macOS:

   ```sh
   python3 src/gamesbyexample/bagels.py
   ```

**Done when:** you play Bagels and guess the secret three-digit number using the clues.

## 6. Build folders using commands (advanced)

Use the terminal to build this structure in your home folder:

```text
terminal-practice/
|-- notes/
`-- projects/
    `-- python/
```

1. Use `cd` to move to your home folder.
2. Make a folder named `terminal-practice`, then move into it.
3. Create the folders shown above.
4. Use `ls` after each step to check your work.

These commands help you. Replace `folder-name` with the folder you want to create or enter.

```sh
cd "$HOME"        # Go to your home folder
cd folder-name    # Go into a folder
cd ..             # Go back up one folder
mkdir folder-name # Create a folder
ls                # List what is in the current folder
```

**Done when:** your final `ls` in `terminal-practice` shows `notes` and `projects`.
