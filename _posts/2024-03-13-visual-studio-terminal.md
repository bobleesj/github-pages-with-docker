---
layout: post
title: Visual Studio and Terminal cheatsheet
categories: cheatsheet
---

## Motivation

I am noticing physical strain on my right pinky finger. Navigating lines of code
is not ergonomic. I am discovering ways to distribute the amount of work done by
my pinky to the left hand.

I minimize mouse and trackpad usage. I maintain my two palms rested without
extending my fingers or hands extended.

Hence, I rely on shortcuts to accomplish efficiency and reduce pain. I have
listed both default and customized shortcuts that I am trying to master and
become embedded in my subconscious brain.

### VS Code customization

One may add customized keyboard shortcuts via `cmd-K`.

### Mastering at the moment

- **Move Line Up/Down:** `ctrl-opt-n/p` (customized)
- **Delete Word Right**: `opt-d` (customized)
- **Cursor Page Up/Down**: `ctrl-cmd-n/p` (customized)
- **Cursor Down Select:** `ctrl-shift-n/p` (customizepd)
- **Delete Word Right**: `ctrl-opt-h` (customized)
- **Delete Right**: `opt-K` (customized)
- **Cursor Word End Right**: `opt-b` (customized)
- **Cursor Word End Left**: `opt-h` (customized)
- **Delete All Left:** `ctrl-shift-h` (customized)
- **Highlight Multiple Lines with Mouse**: `shift-opt-mouse-drag`
- **Duplicate a Line**: `opt-shift-↑/↓`
- **Highlight a Line**: `cmd-l`
- **Remove Line Space Below**: `ctrl-j`
- **Copy a Line(s) Without Highlighting**: `cmd-c`
- **Multiple Cursors via Mouse**: `opt-mouse-click`
- **Move to the Previous Cursor Position**: `cmd-u`
- **Multiple Lines Edit**: `opt-shift-i`

### Code editing

- **Navigate to Line Ends**: `ctrl-a` or `e`
- **Switch Lines**: `opt-↑/↓`
- **Modify Identical Words**: `cmd-shift-l`
- **Remove Characters Left/Right**: `ctrl-h` / `ctrl-d`
- **Delete Line**: `cmd-shift-K`

### Running code

- **Execute Python Code**: `fn-ctr-5`

## Navigation within the editor

- **Delete Text to the Right**: `ctrl-k`
- **Move Cursor by One Line**: `ctrl-p/n` instead of `↑/↓`
- **Browse Files**: `cmd-p`
- **Browse Plugins**: `cmd-shift-p`
- **Create New Panels**: `cmd-1/2/3/4`
- **Duplicate Current Panel**: `ctrl-\`
- **Switch Panel Focus**: `cmd-k-(→ or ←)`
- **Toggle Explorer**: `cmd-b`
- **Find Across All Files**: `cmd-shift-f`
- **Navigate Tabs**: `cmd-shift-]/[`
- **Go to a Specific Line**: `ctrl-G`
- **Word Wrap**: `opt-Z`

### Terminal usage

- **Toggle Terminal**: `cmd-j`

### Global modifications

- **Replace Globally**: `cmd-F12`

## Terminal

### Zip

`zip` combines files with compression. Use `zip` for cross-platform
compatibility.

- `zipinfo directory.zip`
- `zip -r directory.zip directory`

### Tar

`tar` combines files without compression. `tar` is primarily used in Unix/Linux
environments. It provides incremental backups.

To tar:

```bash
tar -cvf born-only.tar /jet/home/sleem/projects/20240218-AlOOH-BORN
tar -cvf born-only.tar
```

To untar:

```bash
tar -xvf born-only.tar
```

For `-cvf` `-c` instructs `tar` to create a new archive, `-v` enables the
verbose mode which displays the progress in the terminal, showing the files
being archived, and `-f` indicates the filename of the archive, which directly
follows this option.

`-xvf` extracts files from a tar archive using `-x` instead of `-c`.

### HPC

The following may not be useful for those who are not using the following HPC
platform.

### Bridges

To make an interative session:

```bash
interact -n 64 -t 8:00:00
```

### Delta

### Phonopy

To add non-analytic correction:

```bash
phonopy-vasp-born > BORN
```

To

```
phonopy -p --nac mesh.conf
```

To plot

```
phonopy-bandplot -o "frequency-born.png" band.yaml
```

### Unix-like OS commands

#### Get folders size

```bash
du -h --max-depth=1 | sort -rh
```

The command `du -h --max-depth=1 | sort -rh` is used in Unix-like operating
systems to list directories and their sizes within the current directory.

- `du`: dist usage
- `-h`: human redable
- `--max-depth=1`: report one level below the current directory
- `sort`: sorts lines of tet
- `-r`: reverse order: largest items first
- `-h`: Sorts numbers with size suffixes (`K`, `M`, `G`)
