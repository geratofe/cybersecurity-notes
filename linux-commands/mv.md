# mv Command

The `mv` command is used to **move or rename files and directories** in Linux.

---

+## Basic Usage

```bash
mv old_name.txt new_name.txt
```

- Renames `old_name.txt` to `new_name.txt`.

```bash
mv file.txt /home/user/Documents/
```

- Moves `file.txt` to the specified directory.

---

+## Options

| Option | Description |
|--------|-------------|
| `-i` | Prompt before overwriting files |
| `-v` | Verbose, shows files being moved |
| `-u` | Move only if the source is newer than the destination |
| `-n` | Do not overwrite existing files |
| `--help` | Show help |

---

+## Examples

- Rename a file:

```bash
mv oldfile.txt newfile.txt
```

- Move a file to another directory:

```bash
mv file.txt /home/user/Documents/
```

- Move multiple files:

```bash
mv file1.txt file2.txt file3.txt /home/user/Documents/
```

- Move with confirmation before overwriting:

```bash
mv -i file.txt /home/user/Documents/
```

- Verbose move:

```bash
mv -v file.txt /tmp/
```

---

+## Pentesting Uses

- **Move sensitive files to a workspace**:

```bash
mv /etc/passwd ~/pentest/backups/
```

- **Rename files to work safely on them**:

```bash
mv sshd_config sshd_config.bak
```

- **Organize collected files**:

```bash
mv *.log ~/pentest/logs/
```

- **Combine with `mkdir` and `touch`**:

```bash
mkdir ~/pentest/backup && mv /var/www/index.php ~/pentest/backup/
```

- **Automation scripts**:

```bash
find /var/log -type f -name "*.log" 2>/dev/null | while read f; do mv "$f" ~/pentest/logs/; done
```

> Moves all `.log` files from `/var/log` to your pentesting folder.

---

+## Notes

- `mv` **does not create a copy** — original file is removed after moving.  
- Always check destination paths to **avoid overwriting important files**.  
- Combine with `&&` or `-i` for safe, automated workflows.  
