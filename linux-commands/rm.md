# rm Command

The `rm` command is used to **remove files and directories** in Linux.  
Be careful — files deleted with `rm` are **not sent to a trash folder** by default.

---

## Basic Usage

```bash
rm file.txt
```
- Removes `file.txt`.

```bash
rm -r folder_name/
```
- Removes a directory and all its contents.

---

## Useful Options

| Option | Description |
|--------|-------------|
| `-r` | Remove directories recursively |
| `-f` | Force deletion without prompts |
| `-i` | Ask before deleting each file |
| `-v` | Show what is being deleted |
| `--help` | Show help |

---

## Examples

- Remove a single file:

```bash
rm notes.txt
```

- Remove multiple files:

```bash
rm file1.txt file2.txt file3.txt
```

- Remove a directory recursively:

```bash
rm -r old_folder/
```

- Remove with confirmation before each file:

```bash
rm -i important_file.txt
```

- Force remove a directory without prompts:

```bash
rm -rf temp_folder/
```

---

## Pentesting / Personal Uses

- Clean up workspace directories:

```bash
rm -r ~/pentest/tmp/
```

- Remove old log files:

```bash
rm ~/pentest/logs/*.log
```

- Combine with `find` to delete specific files:

```bash
find /var/log -type f -name "*.log" 2>/dev/null -exec rm {} \;
```

> Deletes all `.log` files found in `/var/log`.
