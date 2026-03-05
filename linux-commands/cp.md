# cp Command

The `cp` command is used to **copy files and directories** in Linux.

---

+## Basic Usage

```bash
cp source_file.txt destination_file.txt
```

- Copies `source_file.txt` to `destination_file.txt`.

```bash
cp file.txt /home/user/Documents/
```

- Copies `file.txt` to the specified directory.

---

+## Options

| Option | Description |
|--------|-------------|
| `-r` or `-R` | Copy directories recursively |
| `-v` | Verbose, shows files being copied |
| `-i` | Prompt before overwriting files |
| `-u` | Copy only if the source is newer than the destination |
| `-p` | Preserve file attributes (timestamps, permissions) |
| `--help` | Show help |

---

+## Examples

- Copy a file:

```bash
cp notes.txt notes_backup.txt
```

- Copy a directory recursively:

```bash
cp -r project_folder/ project_folder_backup/
```

- Copy with confirmation before overwriting:

```bash
cp -i file.txt /home/user/Documents/
```

- Copy only newer files:

```bash
cp -u file.txt /home/user/Documents/
```

- Copy preserving timestamps and permissions:

```bash
cp -p file.txt /home/user/Documents/
```

---

+## Pentesting Uses

- **Backup important files** before editing:

```bash
cp /etc/passwd /tmp/passwd.bak
```

- **Copy configuration files** for analysis:

```bash
cp /etc/ssh/sshd_config ~/pentest/ssh_configs/
```

- **Duplicate directories** to work on them safely:

```bash
cp -r /var/www/ /tmp/www_backup/
```

- **Combine with `grep` or `find`**:

```bash
find /var/log -type f -name "*.log" 2>/dev/null | while read f; do cp "$f" ~/pentest/logs/; done
```

> Collects all `.log` files from `/var/log` into your pentesting folder.

---

+## Notes

- Always check **destination path** to avoid accidental overwriting.  
- Using `cp -r` is crucial for **copying directories with content**.  
- Combine with `&&` or `>>` in scripts for **automation or logging**.  
