# shred Command

The `shred` command is used to **securely delete files** by overwriting them multiple times before removal.  
Useful when you don’t want deleted files to be recoverable.

---

## Basic Usage

```bash
shred file.txt
```
- Overwrites `file.txt` 3 times (default) but **does not delete it** by default.

```bash
shred -u file.txt
```
- Overwrites and **removes** the file after shredding.

---

## Useful Options

| Option | Description |
|--------|-------------|
| `-u` | Remove the file after overwriting |
| `-n <number>` | Number of overwrite passes (default is 3) |
| `-v` | Verbose, shows progress |
| `-z` | Overwrite with zeros after random passes (makes it look cleaner) |
| `--help` | Show help |

---

## Examples

- Shred a file securely:

```bash
shred file.txt
```

- Shred and delete a file:

```bash
shred -u file.txt
```

- Shred a file with 5 passes and verbose output:

```bash
shred -u -n 5 -v secret.txt
```

- Shred a file and overwrite with zeros after:

```bash
shred -u -z confidential.doc
```

---

## Pentesting / Personal Uses

- Securely delete **sensitive logs or backups**:

```bash
shred -u ~/pentest/logs/secret.log
```

- Remove **configuration files safely**:

```bash
shred -u /tmp/ssh_config_copy
```

- Combine with `find` to shred multiple files:

```bash
find ~/pentest/logs -type f -name "*.log" 2>/dev/null -exec shred -u {} \;
```

> Overwrites and deletes all `.log` files in the pentesting logs folder.
