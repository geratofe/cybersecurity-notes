# Touch and Mkdir Commands

This file covers both `mkdir` (make directories) and `touch` (create empty files or update timestamps).  
These commands are basic but very useful in **Linux scripting, automation, and pentesting**.

---

+## mkdir Command

+`mkdir` is used to create **directories** in Linux.

+### Basic Usage

```bash
mkdir new_folder
```

Creates a directory called `new_folder`.

+### Options

| Option | Description |
|--------|-------------|
| `-p` | Create nested directories (parents) |
| `-v` | Verbose output (shows what is created) |
| `-m` | Set permissions for the directory |
| `--help` | Show help |

+### Examples

- Create a single directory:

```bash
mkdir test_folder
```

- Create nested directories:

```bash
mkdir -p folder1/folder2/folder3
```

- Create a directory and see confirmation:

```bash
mkdir -v my_folder
```

- Create multiple directories at once:

```bash
mkdir folderA folderB folderC
```

+### Pentesting Uses

- Quickly create **workspace directories**:

```bash
mkdir pentest_reports && cd pentest_reports
```

- Organize **collected files**:

```bash
mkdir screenshots logs exploits
```

---

+## touch Command

+`touch` is used to **create empty files** or **update timestamps** of existing files.

+### Basic Usage

```bash
touch file.txt
```

- Creates an empty file called `file.txt`

+### Options

| Option | Description |
|--------|-------------|
| `-c` | Do not create if the file doesn’t exist |
| `-t [[CC]YY]MMDDhhmm[.ss]` | Set a specific timestamp |
| `-a` | Change only the access time |
| `-m` | Change only the modification time |
| `--help` | Show help |

+### Examples

- Create multiple files:

```bash
touch file1.txt file2.txt file3.txt
```

- Update the timestamp of an existing file:

```bash
touch -m existing_file.txt
```

---

+## Combined mkdir + touch

- Create a directory and a file inside in **one line**:

```bash
mkdir new_folder && touch new_folder/newfile.txt
```

- Create multiple directories and files:

```bash
mkdir folder1 folder2 && touch folder1/file1.txt folder2/file2.txt
```

- Useful for **scripts or pentesting setups**:

```bash
mkdir pentest_reports screenshots logs && touch pentest_reports/README.md logs/log.txt
```

- Combine with `&&` for **safe execution**:

```bash
mkdir important_folder && touch important_folder/notes.txt && echo "Setup complete"
```

---

+## Notes

- `mkdir` → **directories**  
- `touch` → **files**  
- Using them together is common in **scripting and pentesting** to quickly create workspaces or collect outputs  
- Combine with other commands (`grep`, `find`) for **automation**  
