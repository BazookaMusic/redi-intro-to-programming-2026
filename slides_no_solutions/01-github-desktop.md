---
theme: ../themes/clio
title: Create a Repository with GitHub Desktop
info: |
  Intro to Programming
  ReDI School 2026
drawings:
  persist: false
transition: slide-left
mdc: true
class: foundation-slide lesson-overview-slide
---

<div class="eyebrow">Git and GitHub</div>

# What will we cover?

<p class="lesson-overview-intro">We will start with the prerequisites, then use Git and GitHub to save and share code.</p>

<div class="lesson-overview-path">
  <section><b>1</b><span><strong>Files and folders</strong>Files, folders, paths, and VS Code</span></section>
  <section><b>2</b><span><strong>Git and GitHub</strong>Repositories, commits, and history</span></section>
  <section><b>3</b><span><strong>Create a repository</strong>GitHub Desktop and publishing online</span></section>
  <section><b>4</b><span><strong>Use the terminal</strong>Clone, pull, add, commit, and push</span></section>
</div>

<p class="lesson-overview-goal"><strong>Goal:</strong> create a Python file, save it with Git, and publish it on GitHub.</p>

---
class: foundation-slide files-slide
---

<div class="eyebrow">Prerequisites</div>

# What is a file?

<p class="foundation-intro">A file is <strong>information stored on a computer and given a name</strong>, so you can find it and use it again later.</p>

<div class="definition-grid">
  <section class="definition-panel">
    <span class="object-label">Inside a file</span>
    <h2>Files are made of bits</h2>
    <p>A <strong>bit</strong> is the smallest piece of computer information. It can be either <code>0</code> or <code>1</code>.</p>
    <p>A file contains many bits. Their pattern can represent words, pictures, sounds, or instructions.</p>
  </section>
  <section class="definition-panel">
    <span class="object-label">What you can do</span>
    <h2>You work with files using apps</h2>
    <p>You can open, change, save, copy, move, share, or delete a file.</p>
    <p>The file stays on your computer until you delete it.</p>
  </section>
</div>

<p class="foundation-note"><code>hello.txt</code> is a file name. <code>hello</code> is the name you choose; <code>.txt</code> is the <strong>file extension</strong>. It indicates that this is a text file and helps the computer choose an app to open it.</p>

---
class: foundation-slide file-examples-slide
---

<div class="eyebrow">Prerequisites</div>

# Text vs Binary files

<div class="file-example-grid">
  <section class="file-example">
    <div class="file-example-heading"><span class="object-label">Text</span><code>hello.txt</code></div>
    <pre class="text-preview">Hello, Ada!
  Have a wonderful day.</pre>
    <p>A text editor like Visual Studio Code shows the file’s characters and lets you edit them.</p>
  </section>
  <section class="file-example">
    <div class="file-example-heading"><span class="object-label">Binary</span><code>crab.png</code></div>
    <div class="app-preview">
      <strong>Can be opened with an image app like Photos</strong>
      <span>The app displays the picture.</span>
    </div>
    <img class="binary-illustration" src="/images/computer-basics/cute-crab.svg" alt="A colorful illustration of a smiling crab">
  </section>
</div>

<style>
.file-example-grid {
  display: grid;
  gap: 1.1rem;
  grid-template-columns: 1fr 1fr;
}

.file-example {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  height: 18rem;
  overflow: hidden;
  padding: 1rem;
}

.file-example-heading {
  align-items: center;
  display: flex;
  justify-content: space-between;
}

.file-example-heading code {
  color: var(--lesson-heading);
  font-size: 0.85rem;
}

.text-preview {
  background: rgb(13 11 31 / 70%);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-ink);
  font-size: 1.1rem;
  line-height: 1.7;
  margin: 1rem 0;
  padding: 1.4rem;
}

.file-example p,
.app-preview span {
  color: var(--lesson-muted);
  font-size: 0.78rem;
}

.app-preview {
  display: grid;
  gap: 0.2rem;
  margin: 0.8rem 0 0.6rem;
}

.app-preview strong {
  color: var(--lesson-blue);
  font-size: 0.78rem;
}

.file-example img {
  border: 1px solid var(--lesson-border);
  height: 10.5rem;
  object-fit: cover;
  object-position: top;
  width: 100%;
}

.file-example img.binary-illustration {
  background: #17132d;
  object-fit: contain;
  object-position: center;
}
</style>

---
class: foundation-slide directory-slide
---

<div class="eyebrow">Prerequisites</div>

# What is a folder?

<div class="directory-definition">
  <div class="directory-mark"><span>Folder</span><strong>project/</strong></div>
  <div class="directory-facts">
    <p><strong>It organizes data</strong><span>A folder holds files and other folders.</span></p>
    <p><strong>It has a name</strong><span>The name helps people and programs find its contents.</span></p>
    <p><strong>It is also called a directory</strong><span>The two words mean the same thing. In this lesson, we will use folder.</span></p>
  </div>
</div>

<style>
.directory-definition {
  align-items: center;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: 0.85fr 1.15fr;
  min-height: 18rem;
}

.directory-mark {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  border-top: 0.8rem solid var(--lesson-blue);
  padding: 2rem 1.6rem;
}

.directory-mark span,
.directory-mark strong,
.directory-facts strong,
.directory-facts span {
  display: block;
}

.directory-mark span {
  color: var(--lesson-muted);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.directory-mark strong {
  color: var(--lesson-heading);
  font-family: monospace;
  font-size: 1.65rem;
  margin-top: 0.55rem;
}

.directory-facts p {
  border-bottom: 1px solid var(--lesson-border);
  margin: 0;
  padding: 0.75rem 0;
}

.directory-facts strong {
  color: var(--lesson-heading);
  font-size: 1rem;
}

.directory-facts span {
  color: var(--lesson-muted);
  font-size: 0.82rem;
  margin-top: 0.2rem;
}
</style>

---
class: foundation-slide directory-example-slide
---

<div class="eyebrow">Prerequisites</div>

# Example: a folder

<div class="directory-example-layout">
  <img class="directory-example-image" src="/images/computer-basics/example-directory.png" alt="A Finder window showing three folders and one image file inside the secrets folder">
  <div class="directory-explanation">
    <p><strong>secrets</strong> is the folder currently open in Finder.</p>
    <p>It contains three folders and one image file.</p>
    <p class="directory-note">The <strong>icons in the image</strong> help us tell them apart: folders have folder icons, while the image file shows a picture thumbnail.</p>
  </div>
</div>

<style>
.directory-example-layout {
  align-items: center;
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1.55fr 0.85fr;
  min-height: 18rem;
}

.directory-example-image {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  width: 100%;
}

.directory-explanation p {
  border-bottom: 1px solid var(--lesson-border);
  color: var(--lesson-muted);
  font-size: 0.95rem;
  line-height: 1.45;
  margin: 0;
  padding: 0.8rem 0;
}

.directory-explanation .directory-note {
  border-left: 3px solid var(--lesson-coral);
  color: var(--lesson-ink);
  padding-left: 0.9rem;
}
</style>

---
class: foundation-slide tree-slide
---

<div class="eyebrow">Prerequisites</div>

# Directories form a tree

<div class="tree-grid">
  <pre class="tree-shell" aria-label="Example folder tree"><span class="tree-folder">~</span>
|-- <span class="tree-folder">Documents/</span>
|   `-- <span class="tree-folder">Projects/</span>
|       `-- <span class="tree-folder">my-website/</span>
|           |-- README.md
|           `-- index.html
`-- <span class="tree-folder">Downloads/</span></pre>
  <div class="tree-terms">
    <p><strong>Parent</strong><span>The folder one level above.</span></p>
    <p><strong>Child</strong><span>A file or folder inside another folder.</span></p>
    <p><strong>Tree</strong><span>The whole branching structure.</span></p>
  </div>
</div>

<p class="foundation-note">Start at the top, then follow one branch to find a file.</p>

<style>
.tree-grid {
  align-items: center;
  display: grid;
  gap: 2rem;
  grid-template-columns: 1.25fr 0.75fr;
}

.tree-shell {
  background: rgb(13 11 31 / 82%);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-ink);
  font-size: 0.95rem;
  line-height: 1.55;
  margin: 0;
  padding: 1.2rem 1.4rem;
}

.tree-folder {
  color: var(--lesson-blue);
  font-weight: 700;
}

.tree-terms p {
  border-bottom: 1px solid var(--lesson-border);
  margin: 0;
  padding: 0.75rem 0;
}

.tree-terms strong,
.tree-terms span {
  display: block;
}

.tree-terms strong {
  color: var(--lesson-heading);
  font-size: 0.95rem;
}

.tree-terms span {
  color: var(--lesson-muted);
  font-size: 0.78rem;
  margin-top: 0.2rem;
}
</style>

---
class: foundation-slide home-slide
---

<div class="eyebrow">Prerequisites</div>

# Your user folder

<div class="home-layout">
  <div class="home-symbol" aria-hidden="true">alex</div>
  <div>
    <p class="home-intro">Every user account has a personal folder for its files and projects.</p>
    <div class="home-paths">
      <div><strong>Windows</strong><code>C:\Users\alex</code></div>
      <div><strong>macOS</strong><code>/Users/alex</code></div>
    </div>
  </div>
</div>

<p class="foundation-note">Your user folder usually contains <strong>Desktop</strong>, <strong>Documents</strong>, and <strong>Downloads</strong>.</p>

<style>
.home-layout {
  align-items: center;
  display: grid;
  gap: 2.4rem;
  grid-template-columns: 0.45fr 1.55fr;
}

.home-symbol {
  color: var(--lesson-blue);
  font-family: "Cinzel", Georgia, serif;
  font-size: 2.4rem;
  line-height: 1;
  text-align: center;
}

.home-intro {
  color: var(--lesson-ink);
  font-size: 1.05rem;
  line-height: 1.45;
  margin: 0 0 1rem;
  opacity: 1;
}

.home-paths div {
  align-items: center;
  border-top: 1px solid var(--lesson-border);
  display: grid;
  grid-template-columns: 6rem 1fr;
  padding: 0.7rem 0;
}

.home-paths strong {
  color: var(--lesson-heading);
}

.home-paths code {
  color: var(--lesson-blue);
}
</style>

---
class: foundation-slide path-slide
---

<div class="eyebrow">Prerequisites</div>

# A path is an address

<p class="path-intro">A path tells the computer exactly where a file or folder lives.</p>

<div class="path-track" aria-label="Windows path to crab.png">
  <span>C:</span><i>\</i><span>Users</span><i>\</i><span>alex</span><i>\</i><span>Documents</span><i>\</i><span>photos</span><i>\</i><strong>crab.png</strong>
</div>

<div class="path-details">
  <p><strong>Start</strong><span><code>C:</code> is the drive.</span></p>
  <p><strong>Follow the folders</strong><span>Open each folder from left to right.</span></p>
  <p><strong>Arrive</strong><span><code>crab.png</code> is the file.</span></p>
</div>

<p class="foundation-note">On macOS, the same idea uses <code>/</code> instead: <code>/Users/alex/Documents/photos/crab.png</code></p>

<style>
.path-intro,
.path-details span {
  color: var(--lesson-ink);
  line-height: 1.45;
}

.path-intro {
  font-size: 1.05rem;
  margin: 0 0 1rem;
  opacity: 1;
}

.path-track {
  align-items: center;
  display: flex;
  gap: 0.45rem;
  margin: 1.8rem 0;
}

.path-track span,
.path-track strong {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-heading);
  font-family: monospace;
  font-size: 0.78rem;
  min-width: 0;
  padding: 0.65rem 0.75rem;
}

.path-track strong {
  border-color: var(--lesson-blue);
  color: var(--lesson-blue);
}

.path-track i {
  color: var(--lesson-blue);
  font-style: normal;
  font-weight: 700;
}

.path-details {
  display: grid;
  gap: 1rem;
  grid-template-columns: 0.75fr 1.4fr 0.75fr;
}

.path-details p {
  border-top: 1px solid var(--lesson-border);
  margin: 0;
  padding-top: 0.75rem;
}

.path-details strong,
.path-details span {
  display: block;
}

.path-details strong {
  color: var(--lesson-heading);
  font-size: 0.9rem;
}

.path-details span {
  font-size: 0.76rem;
  margin-top: 0.2rem;
}
</style>

---
class: foundation-slide create-file-walkthrough-slide
---

<div class="eyebrow">VS Code · Step by step</div>

# Opening a project and creating a file

<div class="create-file-flow">
  <figure class="create-file-step open-folder-step">
    <figcaption><b>1</b><span>In VS Code, choose <strong>File → Open Folder…</strong></span></figcaption>
    <div class="create-file-shot"><img src="/images/computer-basics/open-folder-vscode.png" alt="The File menu in VS Code with Open Folder highlighted"></div>
  </figure>
  <figure class="create-file-step choose-folder-step">
    <figcaption><b>2</b><span>Select your project folder. Click <strong>Open</strong> on macOS or <strong>Select Folder</strong> on Windows.</span></figcaption>
    <div class="create-file-shot"><img src="/images/computer-basics/go-to-folder.png" alt="A folder picker with the project folder selected and the Open button visible"></div>
  </figure>
  <figure class="create-file-step create-button-step">
    <figcaption><b>3</b><span>In Explorer, click <strong>New File</strong>.</span></figcaption>
    <div class="create-file-shot"><img src="/images/computer-basics/create-file.png" alt="The New File button highlighted in the VS Code Explorer"></div>
  </figure>
  <figure class="create-file-step name-file-step">
    <figcaption><b>4</b><span>Type <code>my-file.py</code>, then press <strong>Enter</strong>.</span></figcaption>
    <div class="create-file-shot"><img src="/images/computer-basics/edit-file.png" alt="Naming a new file my-file.py in the VS Code Explorer"></div>
  </figure>
  <figure class="create-file-step edit-file-step">
    <figcaption><b>5</b><span>Type <code>print("hello")</code>, then save.</span></figcaption>
    <div class="create-file-shot"><img src="/images/computer-basics/add-name.png" alt="Editing my-file.py with print hello in VS Code"></div>
  </figure>
</div>

<style>
.create-file-walkthrough-slide {
  padding: 1.2rem 2rem;
}

.create-file-walkthrough-slide h1 {
  font-size: 1.8rem;
  margin: 0.1rem 0 0.55rem;
}

.create-file-flow {
  display: grid;
  gap: 0.55rem;
  grid-template-columns: repeat(6, 1fr);
}

.create-file-step {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  grid-column: span 2;
  margin: 0;
  overflow: hidden;
  padding: 0.45rem;
}

.open-folder-step,
.choose-folder-step {
  grid-column: span 3;
}

.create-file-step figcaption {
  align-items: center;
  display: flex;
  gap: 0.4rem;
  min-height: 2rem;
}

.create-file-step b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: flex;
  flex: 0 0 1.35rem;
  font-size: 0.7rem;
  height: 1.35rem;
  justify-content: center;
}

.create-file-step figcaption span {
  color: var(--lesson-muted);
  font-size: 0.62rem;
  line-height: 1.2;
}

.create-file-step strong {
  color: var(--lesson-heading);
}

.create-file-step code {
  color: var(--lesson-blue);
  font-size: 0.58rem;
}

.create-file-shot {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  height: 8.5rem;
  overflow: hidden;
  width: 100%;
}

.open-folder-step .create-file-shot,
.choose-folder-step .create-file-shot {
  height: 9.5rem;
}

.create-file-shot img {
  display: block;
  height: 100%;
  object-fit: cover;
  object-position: left top;
  width: 100%;
}

.choose-folder-step img {
  object-position: center 68%;
}

.name-file-step img {
  object-position: left center;
}

.edit-file-step img {
  object-position: center;
}
</style>

---
class: knowledge-check-slide
---

<div class="eyebrow">Exercise · Prerequisites</div>

# Read this folder structure

<p class="knowledge-check-intro">Study the tree, then answer the four questions.</p>

<div class="knowledge-check-layout">
<pre class="knowledge-check-tree">my-project/
|-- hello.py
|-- notes.txt
`-- images/
    `-- logo.png</pre>

<ol class="knowledge-questions">
  <li><b>1</b><span>Name the <strong>three files</strong>.</span></li>
  <li><b>2</b><span>Name the <strong>two folders</strong>.</span></li>
  <li><b>3</b><span>What is the file extension of <code>hello.py</code>?</span></li>
  <li><b>4</b><span>What path leads from <code>my-project</code> to <code>logo.png</code>?</span></li>
</ol>
</div>



---
layout: cover
---

<div class="eyebrow">GitHub Desktop · Step by step</div>

# Create your first repository

<p class="lead">
  Make a project on your computer, publish it to GitHub,<br>
  and open it in Visual Studio Code.
</p>

<div class="route" aria-label="Lesson steps">
  <span><b>1</b> Create</span>
  <i>→</i>
  <span><b>2</b> Name</span>
  <i>→</i>
  <span><b>3</b> Publish</span>
  <i>→</i>
  <span><b>4</b> Open</span>
</div>

---
layout: center
class: concept-slide git-intro-slide
---

<div class="eyebrow">Before we create a repository</div>

# Git and GitHub.com

<div class="places">
  <div>
    <span class="place-number">01</span>
    <h2>Git</h2>
    <p>A tool on your computer that records changes to a project. It lets you see what changed and return to an earlier version.</p>
  </div>
  <div>
    <span class="place-number">02</span>
    <h2>GitHub</h2>
    <p>A website that stores Git projects online. It lets you share your work and collaborate with other people.</p>
  </div>
</div>

<p class="prerequisite"><strong>How will we use them?</strong> Git keeps the history, and GitHub keeps an online copy. We will create and publish the repository with GitHub Desktop, then use Git by typing commands in VS Code’s terminal.</p>

<style>
.git-intro-slide h1 {
  font-family: system-ui, sans-serif;
  font-weight: 750;
  letter-spacing: 0;
}
</style>

---
class: foundation-slide repository-intro-slide
---

<div class="eyebrow">A new word</div>

# What is a repository?

<p class="foundation-intro">A <strong>repository</strong>, or <strong>repo</strong>, is a project folder that Git keeps track of.</p>

<div class="repository-parts">
  <section>
    <span class="object-label">Your project</span>
    <h2>The files you work on</h2>
    <p>It contains the code, images, notes, and other files that belong to one project.</p>
  </section>
  <section>
    <span class="object-label">Git</span>
    <h2>A history of changes</h2>
    <p>Each saved point in the project’s history is called a <strong>commit</strong>. Commits show what changed, who changed it, and when.</p>
  </section>
</div>

<p class="foundation-note">A repository can be on your computer, on GitHub.com, or in both places.</p>

<style>
.repository-intro-slide h1 {
  font-family: system-ui, sans-serif;
  font-weight: 750;
  letter-spacing: 0;
}

.repository-parts {
  display: grid;
  gap: 1.1rem;
  grid-template-columns: 1fr 1fr;
}

.repository-parts section {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  min-height: 12rem;
  padding: 1.45rem;
}

.repository-parts h2 {
  font-size: 1.25rem;
  margin: 0.45rem 0 0.7rem;
}

.repository-parts p {
  color: var(--lesson-muted);
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
}
</style>

---
class: commits-tour-slide
---

<div class="eyebrow">See a repository online</div>

# Where are the commits?

<p class="repository-link">
  <strong>Our course repository</strong>
  <a href="https://github.com/BazookaMusic/redi-intro-to-programming-2026" target="_blank">https://github.com/BazookaMusic/redi-intro-to-programming-2026</a>
</p>

<div class="commit-tour">
  <figure>
    <figcaption><b>1</b> Open the repository and click the <strong>commits link</strong>.</figcaption>
    <img src="/images/github/commits-open.png" alt="The repository main page with the commits link visible">
  </figure>
  <figure>
    <figcaption><b>2</b> GitHub shows the project’s commit history.</figcaption>
    <img src="/images/github/commits-main-page.png" alt="The repository commits page showing the project history">
  </figure>
</div>

<style>
.commits-tour-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 2.3rem;
  font-weight: 750;
  letter-spacing: 0;
  margin-bottom: 0.2rem;
}

.repository-link {
  display: flex;
  flex-direction: column;
  font-size: 0.95rem;
  gap: 0.15rem;
  margin: 0.35rem 0 0;
}

.repository-link strong {
  color: #ffffff;
  font-size: 1.05rem;
}

.repository-link a {
  color: var(--lesson-link);
  font-weight: 750;
  text-decoration: underline;
  text-decoration-color: var(--lesson-blue);
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}

.commit-tour {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr 1fr;
  margin-top: 1rem;
}

.commit-tour figure {
  margin: 0;
  min-width: 0;
}

.commit-tour figcaption {
  font-size: 0.9rem;
  line-height: 1.45;
  margin-bottom: 0.5rem;
}

.commit-tour figcaption b {
  align-items: center;
  background: var(--lesson-coral);
  border-radius: 50%;
  color: white;
  display: inline-flex;
  height: 1.55rem;
  justify-content: center;
  margin-right: 0.45rem;
  vertical-align: middle;
  width: 1.55rem;
}

.commit-tour img {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  display: block;
  max-height: 13.3rem;
  object-fit: contain;
  object-position: top left;
  width: 100%;
}
</style>

---
class: knowledge-check-slide
---

<div class="eyebrow">Exercise · Git and GitHub</div>

# Choose the right word

<p class="knowledge-check-intro">Use each answer once: <strong>Git</strong>, <strong>GitHub</strong>, <strong>repository</strong>, <strong>commit</strong>.</p>

<ol class="knowledge-questions knowledge-questions-wide">
  <li><b>1</b><span>The tool that records changes on your computer is ______.</span></li>
  <li><b>2</b><span>A project folder that Git tracks is a ______.</span></li>
  <li><b>3</b><span>A saved point in the project’s history is a ______.</span></li>
  <li><b>4</b><span>The website where you publish and share Git projects is ______.</span></li>
</ol>



---
class: step-slide
---

<div class="step-label">Step 1 of 4</div>

# Start a new repository

<div class="step-grid wide-shot">
  <div class="step-copy">
    <span class="action">First</span>
    <p>Open <strong>GitHub Desktop</strong>.</p>
    <p>Then choose <strong>File</strong> → <strong>New Repository…</strong></p>
    <p class="hint">A repository is the project folder Git will track.</p>
  </div>
  <img src="/images/github/new-repo.png" alt="The File menu in GitHub Desktop with New Repository selected">
</div>

---
class: step-slide
---

<div class="step-label">Step 2 of 4</div>

# Choose the repository details

<div class="step-grid form-shot">
  <div class="step-copy checklist">
    <p><b>1.</b> Give the repository a short, clear name.</p>
    <p><b>2.</b> Choose where to save it.</p>
    <p><b>3.</b> Tick the box to initialize with a readme.</p>
    <p class="finish">Click <strong>Create Repository</strong>.</p>
  </div>
  <img src="/images/github/new-repo-card.png" alt="The Create a New Repository form in GitHub Desktop">
</div>

---
layout: center
class: pause-slide
---

<div class="eyebrow">Pause and check</div>

# Your repository now exists locally

<p class="lead">GitHub Desktop created the project folder on your computer.</p>

<div class="status-line">
  <span>✓ Folder created</span>
  <span>✓ Git history started</span>
  <span class="pending">○ Not online yet</span>
</div>

---
class: step-slide
---

<div class="step-label">Step 3 of 4</div>

# Publish it to GitHub

<div class="publish-flow">
  <figure>
    <figcaption><b>1</b> Click <strong>Publish repository</strong> in the top bar.</figcaption>
    <img src="/images/github/main-view-with-publish.png" alt="The GitHub Desktop main view with Publish repository in the top bar">
  </figure>
  <figure>
    <figcaption><b>2</b> Review the name, description, and visibility. Then click <strong>Publish Repository</strong>.</figcaption>
    <img src="/images/github/publish-repo.png" alt="The Publish Repository form in GitHub Desktop">
  </figure>
</div>

<style>
.publish-flow {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1.15fr 0.85fr;
  margin-top: 1rem;
}

.publish-flow figure {
  margin: 0;
  min-width: 0;
}

.publish-flow figcaption {
  font-size: 0.9rem;
  line-height: 1.4;
  margin-bottom: 0.5rem;
  min-height: 2.6rem;
}

.publish-flow figcaption b {
  align-items: center;
  background: var(--lesson-coral);
  border-radius: 50%;
  color: #17112f;
  display: inline-flex;
  height: 1.55rem;
  justify-content: center;
  margin-right: 0.35rem;
  width: 1.55rem;
}

.publish-flow img {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  display: block;
  height: 14rem;
  object-fit: contain;
  object-position: top center;
  width: 100%;
}
</style>

---
class: step-slide
---

<div class="step-label">Step 4 of 4</div>

# Open the project in VS Code

<div class="step-grid wide-shot">
  <div class="step-copy">
    <span class="action">Open</span>
    <p><strong>Repository</strong> → <strong>Open in Visual Studio Code</strong></p>
    <p class="hint">Now you can create files and begin coding inside the repository.</p>
  </div>
  <img src="/images/github/open-in-vscode.png" alt="The Repository menu in GitHub Desktop with Open in Visual Studio Code selected">
</div>

---
class: exercise-slide
---

<div class="eyebrow">Exercise</div>

# Create and publish your repository

<div class="exercise-grid">
  <section class="exercise-step">
    <div class="exercise-copy">
      <b>1</b>
      <div><h2>Create</h2><p><strong>File</strong> → <strong>New Repository…</strong></p></div>
    </div>
    <img src="/images/github/new-repo.png" alt="File menu with New Repository selected">
  </section>
  <section class="exercise-step">
    <div class="exercise-copy">
      <b>2</b>
      <div><h2>Set up</h2><p>Name it, choose a folder, and add a README.</p></div>
    </div>
    <img src="/images/github/new-repo-card.png" alt="Create a New Repository form">
  </section>
  <section class="exercise-step">
    <div class="exercise-copy">
      <b>3</b>
      <div><h2>Publish</h2><p>Click <strong>Publish repository</strong>.</p></div>
    </div>
    <img src="/images/github/publish-repo.png" alt="Publish Repository form">
  </section>
  <section class="exercise-step">
    <div class="exercise-copy">
      <b>4</b>
      <div><h2>Open</h2><p><strong>Repository</strong> → <strong>Open in Visual Studio Code</strong></p></div>
    </div>
    <img src="/images/github/open-in-vscode.png" alt="Repository menu with Open in Visual Studio Code selected">
  </section>
</div>

<p class="exercise-done"><strong>Done when:</strong> your repository is online and open in VS Code.</p>

---
layout: center
class: finish-slide
---

<div class="eyebrow">Repository ready</div>

# You made it

<div class="recap">
  <span><b>1</b> Created locally</span>
  <span><b>2</b> Published online</span>
  <span><b>3</b> Opened in VS Code</span>
</div>

<div class="repository-address">
  <span>Open your repository in your browser (e.g. Chrome, Edge, or Safari) at:</span>
  <code>www.github.com/<mark>username</mark>/<mark>name-of-your-repo</mark></code>
  <p>Replace <strong>username</strong> with your GitHub username and <strong>name-of-your-repo</strong> with your repository name.</p>
  <p class="repository-example"><strong>Example:</strong> <a href="https://github.com/bazookamusic/redi-example" target="_blank">www.github.com/bazookamusic/redi-example</a></p>
</div>

<p class="lead">Next: create a file inside your repository.</p>

<style>
.repository-address {
  margin: 1.5rem 0 1.1rem;
}

.repository-address > span {
  display: block;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
}

.repository-address code {
  background: rgb(4 16 26 / 62%);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: #ffffff;
  display: inline-block;
  font-size: 1.15rem;
  padding: 0.5rem 0.7rem;
}

.repository-address mark {
  background: transparent;
  color: var(--lesson-blue);
  font-weight: 800;
}

.repository-address p {
  font-size: 0.85rem;
  margin: 0.45rem 0 0;
}

.repository-example a {
  color: #ffffff;
  text-decoration-color: var(--lesson-blue);
  text-decoration-thickness: 2px;
  text-underline-offset: 0.16em;
}

.step-label {
  color: var(--lesson-coral);
  font-size: 0.8rem;
  font-weight: 750;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.route {
  align-items: center;
  display: flex;
  gap: 1rem;
  margin-top: 4.25rem;
}

.route span {
  align-items: center;
  display: flex;
  font-size: 1.05rem;
  font-weight: 650;
  gap: 0.55rem;
}

.route b,
.recap b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: inline-flex;
  height: 2rem;
  justify-content: center;
  width: 2rem;
}

.route i {
  color: #b9a3e3;
  font-style: normal;
}

.concept-slide,
.pause-slide,
.finish-slide {
  text-align: left;
}

.places {
  border-bottom: 1px solid var(--lesson-border);
  border-top: 1px solid var(--lesson-border);
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-top: 2rem;
}

.places>div {
  padding: 1.4rem 2rem 1.4rem 0;
}

.places>div+div {
  border-left: 1px solid var(--lesson-border);
  padding-left: 2rem;
}

.places p,
.prerequisite {
  color: var(--lesson-muted);
  line-height: 1.45;
}

.place-number {
  color: var(--lesson-blue);
  font-size: 0.85rem;
  font-weight: 750;
}

.prerequisite {
  font-size: 0.95rem;
  margin-top: 1.4rem;
}

.foundation-slide {
  padding: 2rem 3rem;
}

.foundation-slide h1 {
  font-size: 2.2rem;
  margin: 0.3rem 0 1.1rem;
}

.foundation-slide .foundation-intro {
  color: var(--lesson-ink);
  font-size: 1.05rem;
  margin: 0 0 1.1rem;
  opacity: 1;
}

.definition-grid,
.file-example-grid {
  display: grid;
  gap: 1.1rem;
  grid-template-columns: 1fr 1fr;
}

.definition-panel {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  min-height: 13rem;
  padding: 1.45rem;
}

.object-label {
  color: var(--lesson-blue);
  font-size: 0.72rem;
  font-weight: 750;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.definition-panel h2 {
  font-size: 1.2rem;
  margin: 0.4rem 0 0.55rem;
}

.definition-panel p,
.home-intro,
.path-intro,
.path-details p {
  color: var(--lesson-ink);
  line-height: 1.45;
}

.definition-panel p {
  font-size: 1rem;
  line-height: 1.55;
  margin: 0 0 0.8rem;
}

.file-example {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  height: 18rem;
  overflow: hidden;
  padding: 1rem;
}

.file-example-heading {
  align-items: center;
  display: flex;
  justify-content: space-between;
}

.file-example-heading code {
  color: var(--lesson-heading);
  font-size: 0.85rem;
}

.text-preview {
  background: rgb(13 11 31 / 70%);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-ink);
  font-size: 1.1rem;
  line-height: 1.7;
  margin: 1rem 0;
  padding: 1.4rem;
}

.file-example p,
.app-preview span {
  color: var(--lesson-muted);
  font-size: 0.78rem;
}

.app-preview {
  display: grid;
  gap: 0.2rem;
  margin: 0.8rem 0 0.6rem;
}

.app-preview strong {
  color: var(--lesson-blue);
  font-size: 0.78rem;
}

.file-example img {
  border: 1px solid var(--lesson-border);
  height: 10.5rem;
  object-fit: cover;
  object-position: top;
  width: 100%;
}

.file-example img.binary-illustration {
  background: #17132d;
  object-fit: contain;
  object-position: center;
}

.directory-definition,
.directory-example-layout {
  align-items: center;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: 0.85fr 1.15fr;
  min-height: 18rem;
}

.directory-example-layout {
  gap: 1.5rem;
  grid-template-columns: 1.55fr 0.85fr;
}

.directory-example-image {
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  width: 100%;
}

.directory-mark {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  border-top: 0.8rem solid var(--lesson-blue);
  padding: 2rem 1.6rem;
}

.directory-mark span,
.directory-mark strong,
.directory-facts strong,
.directory-facts span {
  display: block;
}

.directory-mark span {
  color: var(--lesson-muted);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.directory-mark strong {
  color: var(--lesson-heading);
  font-family: monospace;
  font-size: 1.65rem;
  margin-top: 0.55rem;
}

.directory-facts p {
  border-bottom: 1px solid var(--lesson-border);
  margin: 0;
  padding: 0.75rem 0;
}

.directory-facts strong {
  color: var(--lesson-heading);
  font-size: 1rem;
}

.directory-facts span,
.directory-explanation>p {
  color: var(--lesson-muted);
  font-size: 0.82rem;
  margin-top: 0.2rem;
}

.directory-explanation>p {
  border-bottom: 1px solid var(--lesson-border);
  font-size: 0.95rem;
  line-height: 1.45;
  margin: 0;
  padding: 0.8rem 0;
}

.directory-explanation .repository-definition,
.foundation-note,
.hint {
  border-left: 3px solid var(--lesson-coral);
  color: var(--lesson-ink);
  padding-left: 0.9rem;
}

.foundation-note {
  font-size: 0.92rem;
  margin: 1rem 0 0;
}

.tree-grid {
  align-items: center;
  display: grid;
  gap: 2rem;
  grid-template-columns: 1.25fr 0.75fr;
}

.tree-shell {
  background: rgb(13 11 31 / 82%);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-ink);
  font-size: 0.95rem;
  line-height: 1.55;
  margin: 0;
  padding: 1.2rem 1.4rem;
}

.tree-folder {
  color: var(--lesson-blue);
  font-weight: 700;
}

.tree-terms p {
  border-bottom: 1px solid var(--lesson-border);
  margin: 0;
  padding: 0.75rem 0;
}

.tree-terms strong,
.tree-terms span {
  display: block;
}

.tree-terms strong {
  color: var(--lesson-heading);
  font-size: 0.95rem;
}

.tree-terms span {
  color: var(--lesson-muted);
  font-size: 0.78rem;
  margin-top: 0.2rem;
}

.home-layout {
  align-items: center;
  display: grid;
  gap: 2.4rem;
  grid-template-columns: 0.45fr 1.55fr;
}

.home-symbol {
  color: var(--lesson-blue);
  font-family: "Cinzel", Georgia, serif;
  font-size: 9rem;
  line-height: 0.8;
  text-align: center;
}

.foundation-slide .home-intro,
.foundation-slide .path-intro {
  font-size: 1.05rem;
  margin: 0 0 1rem;
  opacity: 1;
}

.home-paths>div {
  align-items: center;
  border-top: 1px solid var(--lesson-border);
  display: grid;
  grid-template-columns: 6rem 1fr;
  padding: 0.7rem 0;
}

.home-paths strong {
  color: var(--lesson-heading);
}

.home-paths code,
.path-details code {
  color: var(--lesson-blue);
}

.path-track {
  align-items: center;
  display: flex;
  gap: 0.7rem;
  margin: 2rem 0;
}

.path-track span {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  color: var(--lesson-heading);
  font-family: monospace;
  font-size: 1rem;
  padding: 0.7rem 0.9rem;
}

.path-track i {
  color: var(--lesson-blue);
  font-style: normal;
  font-weight: 700;
}

.path-details {
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr 1fr;
}

.path-details>div {
  border-top: 1px solid var(--lesson-border);
  padding-top: 0.8rem;
}

.path-details p {
  font-size: 0.82rem;
  margin: 0.45rem 0;
}

.path-details code {
  font-size: 0.85rem;
}

.step-grid {
  align-items: center;
  display: grid;
  gap: 2.25rem;
  grid-template-columns: minmax(13rem, 0.7fr) minmax(0, 1.7fr);
  height: 22.75rem;
}

.step-grid img {
  border: 1px solid var(--lesson-border);
  box-shadow: 0 18px 40px rgb(7 4 17 / 45%);
  justify-self: center;
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}

.form-shot {
  grid-template-columns: minmax(16rem, 0.9fr) minmax(0, 1.1fr);
}

.publish-shot {
  grid-template-columns: minmax(15rem, 0.8fr) minmax(0, 1.35fr);
}

.step-copy {
  font-size: 1.1rem;
  line-height: 1.45;
}

.step-copy p {
  margin: 0 0 1rem;
}

.action {
  color: var(--lesson-blue);
  display: block;
  font-size: 0.8rem;
  font-weight: 750;
  letter-spacing: 0.12em;
  margin-bottom: 0.6rem;
  text-transform: uppercase;
}

.hint {
  color: var(--lesson-muted);
  font-size: 0.9rem;
}

.checklist {
  font-size: 0.9rem;
}

.checklist b {
  color: var(--lesson-blue);
}

.checklist .finish {
  border-top: 1px solid var(--lesson-border);
  color: var(--lesson-ink);
  margin-top: 1.2rem;
  padding-top: 1rem;
}

.status-line,
.recap {
  display: flex;
  gap: 1rem;
  margin-top: 2.5rem;
}

.status-line span {
  border-bottom: 3px solid var(--lesson-green);
  font-size: 1rem;
  font-weight: 650;
  padding: 0.8rem 0;
}

.status-line .pending {
  border-color: var(--lesson-coral);
}

.recap span {
  align-items: center;
  display: flex;
  font-size: 1.05rem;
  font-weight: 650;
  gap: 0.65rem;
}

.finish-slide .lead {
  margin-top: 3rem;
}

.exercise-slide {
  padding: 1.8rem 2.4rem;
}

.exercise-slide h1 {
  font-size: 2rem;
  margin: 0.2rem 0 0.9rem;
}

.exercise-grid {
  display: grid;
  gap: 0.75rem;
  grid-template-columns: 1fr 1fr;
}

.exercise-step {
  align-items: stretch;
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  display: grid;
  gap: 0.7rem;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.15fr);
  height: 9.5rem;
  overflow: hidden;
  padding: 0.65rem;
}

.exercise-copy {
  align-items: flex-start;
  display: flex;
  gap: 0.55rem;
}

.exercise-copy>b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: flex;
  flex: 0 0 1.65rem;
  font-size: 0.85rem;
  height: 1.65rem;
  justify-content: center;
}

.exercise-copy h2 {
  font-size: 1rem;
  margin: 0.1rem 0 0.35rem;
}

.exercise-copy p {
  color: var(--lesson-muted);
  font-size: 0.72rem;
  line-height: 1.35;
  margin: 0;
}

.exercise-step img {
  align-self: center;
  border: 1px solid var(--lesson-border);
  height: 100%;
  max-width: 100%;
  object-fit: contain;
  width: 100%;
}

.exercise-done {
  color: var(--lesson-green);
  font-size: 0.85rem;
  margin: 0.7rem 0 0;
  text-align: center;
}
</style>

---
class: create-repository-file-slide
---

<div class="eyebrow">Your turn · VS Code</div>

# Create a file in your repository

<p class="create-repository-file-intro">Your repository is already open in VS Code. Now add your first Python file.</p>

<div class="create-repository-file-flow">
  <figure>
    <figcaption><b>1</b><span>In Explorer, click <strong>New File</strong>.</span></figcaption>
    <img src="/images/computer-basics/create-file.png" alt="The New File button highlighted in the VS Code Explorer">
  </figure>
  <figure>
    <figcaption><b>2</b><span>Type <code>my-file.py</code>, then press <strong>Enter</strong>.</span></figcaption>
    <img src="/images/computer-basics/edit-file.png" alt="Naming a new file my-file.py in the VS Code Explorer">
  </figure>
  <figure>
    <figcaption><b>3</b><span>Type <code>print("hello")</code>, then save.</span></figcaption>
    <img src="/images/computer-basics/add-name.png" alt="Editing my-file.py with print hello in VS Code">
  </figure>
</div>

<p class="create-repository-file-done"><strong>Done when:</strong> <code>my-file.py</code> appears inside your repository folder.</p>

<style>
.create-repository-file-slide {
  padding: 1.5rem 2rem;
}

.create-repository-file-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 2rem;
  letter-spacing: 0;
  margin: 0.15rem 0 0.3rem;
}

.create-repository-file-intro {
  font-size: 0.9rem;
  margin: 0 0 0.8rem;
}

.create-repository-file-flow {
  display: grid;
  gap: 0.75rem;
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.create-repository-file-flow figure {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  margin: 0;
  min-width: 0;
  overflow: hidden;
  padding: 0.5rem;
}

.create-repository-file-flow figcaption {
  align-items: center;
  display: flex;
  font-size: 0.72rem;
  gap: 0.4rem;
  line-height: 1.3;
  min-height: 2.7rem;
}

.create-repository-file-flow figcaption b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: inline-flex;
  flex: 0 0 1.4rem;
  height: 1.4rem;
  justify-content: center;
}

.create-repository-file-flow img {
  border: 1px solid var(--lesson-border);
  border-radius: 4px;
  display: block;
  height: 11.5rem;
  object-fit: cover;
  object-position: left center;
  width: 100%;
}

.create-repository-file-flow figure:last-child img {
  object-position: center;
}

.create-repository-file-done {
  color: var(--lesson-green);
  font-size: 0.85rem;
  margin: 0.7rem 0 0;
  text-align: center;
}
</style>

---
class: open-terminal-slide
---

<div class="eyebrow">VS Code · Step by step</div>

# Open the terminal

<p class="open-terminal-intro">The terminal lets you give text commands to your computer without leaving VS Code.</p>

<div class="open-terminal-flow">
  <figure>
    <figcaption><b>1</b><span>Choose <strong>Terminal → New Terminal</strong>.</span></figcaption>
    <img src="/images/github/click-terminal.png" alt="The VS Code Terminal menu with New Terminal selected">
  </figure>
  <figure>
    <figcaption><b>2</b><span>The terminal opens at the bottom of VS Code.</span></figcaption>
    <img src="/images/github/terminal-bottom.png" alt="The terminal panel open at the bottom of VS Code">
  </figure>
</div>

<p class="open-terminal-done"><strong>Check:</strong> the terminal shows the name of your repository next to the prompt.</p>

<style>
.open-terminal-slide {
  padding: 1.5rem 2rem;
}

.open-terminal-slide h1 {
  font-family: system-ui, sans-serif;
  font-size: 2rem;
  letter-spacing: 0;
  margin: 0.15rem 0 0.3rem;
}

.open-terminal-intro {
  font-size: 0.9rem;
  margin: 0 0 0.8rem;
}

.open-terminal-flow {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: 1fr 1fr;
}

.open-terminal-flow figure {
  background: var(--lesson-panel);
  border: 1px solid var(--lesson-border);
  border-radius: 6px;
  margin: 0;
  min-width: 0;
  overflow: hidden;
  padding: 0.5rem;
}

.open-terminal-flow figcaption {
  align-items: center;
  display: flex;
  font-size: 0.82rem;
  gap: 0.45rem;
  line-height: 1.3;
  min-height: 2.4rem;
}

.open-terminal-flow figcaption b {
  align-items: center;
  background: var(--lesson-blue);
  border-radius: 50%;
  color: #17112f;
  display: inline-flex;
  flex: 0 0 1.5rem;
  height: 1.5rem;
  justify-content: center;
}

.open-terminal-flow img {
  border: 1px solid var(--lesson-border);
  border-radius: 4px;
  display: block;
  height: 15rem;
  object-fit: cover;
  object-position: top left;
  width: 100%;
}

.open-terminal-flow figure:last-child img {
  object-position: bottom center;
  transform: scale(1.65);
  transform-origin: bottom left;
}

.open-terminal-done {
  color: var(--lesson-green);
  font-size: 0.85rem;
  margin: 0.7rem 0 0;
  text-align: center;
}
</style>

---
class: git-command-sequence-slide git-stage-slide
---

<div class="eyebrow">Terminal · Save and publish</div>

# 1. Check and stage the file

<p class="git-command-intro">Type or copy one command at a time. <strong>Press Enter after each command</strong> to run it.</p>

<div class="git-command-panels git-command-panels-wide-first">
<section>

## Check what Git sees

```bash
git status
```

<pre class="command-output">On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add &lt;file&gt;..." to include in what will be committed)
  <span class="git-untracked">hello.py</span>

nothing added to commit but untracked files present
(use "git add" to track)</pre>

<p><strong>What it means:</strong> The red filename means <code>hello.py</code> is untracked. Red does not mean it is broken.</p>
</section>

<section>

## Stage the file

```bash
git add .
```

<pre class="command-output">No output appears.
The prompt returns.</pre>

<p><strong>What it means:</strong> <code>git add</code> chooses which changes Git will include in your next commit.<br><strong>The dot <code>.</code></strong> means every changed file in this repository.<br><strong>To choose only <code>hello.py</code>, use its path from the repository folder:</strong></p>

<div class="git-single-file-option">

```bash
git add ./hello.py
```

</div>
</section>
</div>

---
class: git-command-sequence-slide
---

<div class="eyebrow">Terminal · Save and publish</div>

# 2. Verify and create a commit

<p class="git-command-intro">Run each command with <strong>Enter</strong>. Your commit code may look different from this example.</p>

<div class="git-command-panels">
<section>

## Check that the file is staged

```bash
git status
```

<pre class="command-output">On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged &lt;file&gt;..." to unstage)
  <span class="git-staged">new file:   hello.py</span></pre>

<p><strong>What it means:</strong> The green filename means the file is staged. It will be included in your next commit.</p>
</section>

<section>

## Save it in Git's history

```bash
git commit -m "Printed hello"
```

<pre class="command-output">[main a4058f0] Printed hello
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py</pre>

<p><strong>What it means:</strong> Git created the commit locally. Your seven-character code will be different.</p>
</section>
</div>

---
class: git-command-sequence-slide
---

<div class="eyebrow">Terminal · Save and publish</div>

# 3. Check and push to GitHub

<p class="git-command-intro">Press <strong>Enter</strong> after each command. Git may print slightly different numbers on your computer.</p>

<div class="git-command-panels">
<section>

## Check the local commit

```bash
git status
```

<pre class="command-output">On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean</pre>

<p><strong>What it means:</strong> The commit exists on your computer, but has not reached GitHub yet.</p>
</section>

<section>

## Send the commit online

```bash
git push
```

<pre class="command-output">Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/username/name-of-your-repo.git
   a1c79f4..a4058f0  main -&gt; main</pre>

<p><strong>What it means:</strong> The progress lines are normal. <code>main → main</code> confirms the commit is now on GitHub.</p>
</section>
</div>

---
class: git-command-sequence-slide git-exercise-slide
---

<div class="eyebrow">Exercise · Work from top to bottom</div>

# Make and publish a commit

<div class="git-exercise-layout">
  <div class="git-exercise-prep">
    <div class="git-exercise-step"><b>1</b><span><strong>Change <code>hello.py</code></strong>Add a new line, for example:<br><code>print("I made a commit!")</code></span></div>
    <div class="git-exercise-step"><b>2</b><span><strong>Save the file</strong>Use <code>Ctrl + S</code> on Windows or <code>⌘ + S</code> on macOS.</span></div>
    <div class="git-exercise-step"><b>3</b><span><strong>Open the terminal</strong>Choose <em>Terminal → New Terminal</em>.</span></div>
    <div class="git-exercise-finish"><strong>Finished?</strong> Open your repository on GitHub and look for the new commit.</div>
  </div>

  <div class="git-exercise-commands">

```bash
# 4. Check what changed
git status

# 5. Choose hello.py for the commit
git add ./hello.py

# 6. Check that hello.py is green
git status

# 7. Create the commit
git commit -m "Update hello"

# 8. Check that the commit is ready
git status

# 9. Send it to GitHub
git push
```

  </div>
</div>

---
class: git-command-sequence-slide git-clone-slide
---

<div class="eyebrow">Terminal · Download a repository</div>

# How do I get a repository from GitHub?

<p class="git-command-intro">Choose where the repository should live before you download it.</p>

<div class="git-clone-workflow">
  <div class="git-clone-step"><b>1</b><span><strong>Open VS Code</strong>Choose <em>File → Open Folder…</em></span></div>
  <div class="git-clone-step"><b>2</b><span><strong>Choose the parent folder</strong>Select <em>Documents</em>, or create a <em>Code</em> folder there.</span></div>
  <div class="git-clone-step"><b>3</b><span><strong>Open the terminal</strong>Choose <em>Terminal → New Terminal</em>. It opens in the selected folder.</span></div>

  <section class="git-clone-command">
    <div class="git-clone-step-heading"><b>4</b><strong>Clone the repository</strong></div>

```bash
git clone https://github.com/username/name-of-your-repo.git
```

  </section>

  <div class="git-clone-step"><b>5</b><span><strong>Open the new repository</strong>Choose <em>File → Open Folder…</em> and select the <code>name-of-your-repo</code> folder.</span></div>

  <section class="git-pull-followup">
    <span><strong>Next time: get updates</strong>Open the repository folder and its terminal, then run:</span>

```bash
git pull
```

  </section>
</div>

---
class: git-command-sequence-slide git-full-sequence-slide
---

<div class="eyebrow">Terminal · Cheat sheet</div>

# Git Cheat Sheet

<p class="git-command-intro">Run these commands one at a time. Press <strong>Enter</strong> after each command.</p>

```bash
# Get a repository for the first time
git clone https://github.com/username/name-of-your-repo.git

# Get its newest changes later
git pull

# 1. Check what Git sees
git status

# 2. Choose hello.py for the next commit
git add ./hello.py

# 3. Check that hello.py was added
git status

# 4. Create the commit
git commit -m "Printed hello"

# 5. Check that the commit is ready to publish
git status

# 6. Send the commit to GitHub
git push
```
