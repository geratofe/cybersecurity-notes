# chmod Command

The `chmod` command is used to **change file or directory permissions** in Linux.  
Permissions control **who can read, write, or execute** a file.

---

## Basic Usage

```bash
chmod 644 file.txt
```
- Sets permissions to **read/write for owner, read-only for group and others**.

```bash
chmod +x script.sh
```
- Adds **execute permission** to a script.

```bash
chmod -R 755 folder_name/
```
- Recursively sets permissions for a folder and all its contents.

---

## Permission Codes

| Code | Meaning |
|------|---------|
| 4    | Read (`r`) |
| 2    | Write (`w`) |
| 1    | Execute (`x`) |
| 0    | No permission |

- Combine numbers: `rwx` → `4+2+1 = 7`  

**Examples:**

- `chmod 700 file.txt` → only owner can read/write/execute  
- `chmod 644 file.txt` → owner read/write, others read  
- `chmod 755 script.sh` → owner rwx, others r-x  

---

## Symbolic Permissions

- `chmod u+x file.txt` → add execute for owner  
- `chmod g-w file.txt` → remove write for group  
- `chmod o=r file.txt` → others can only read  

---

## Pentesting / Personal Uses

- Make a script executable:

```bash
chmod +x exploit.sh
```

- Secure sensitive files:

```bash
chmod 600 secret.txt
```

- Set permissions for directories recursively:

```bash
chmod -R 700 ~/pentest/
```

- Combine with `find` to fix permissions on multiple files:

```bash
find ~/pentest/ -type f -name "*.sh" 2>/dev/null -exec chmod +x {} \;
```

> Makes all `.sh` files in your pentesting folder executable.

---

## Notes / Tips

- Always double-check permissions before running scripts.  
- Use **numeric codes** for scripts or automated tasks; symbolic for **quick edits**.  
- `chmod` is essential for **pentesting labs**, managing access to scripts, exploits, and logs.
