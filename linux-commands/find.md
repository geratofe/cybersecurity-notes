# 🧠 Linux `find` Command 

The `find` command is one of the most powerful tools in Linux. It is used to **search for files and directories** based on conditions like name, size, type, permissions, ownership, and more.

---

## 📌 Basic Syntax

```bash
find [path] [options] [expression]
```

* **path** → where the search starts
* **options** → control behavior
* **expression** → filters (name, size, etc.)

---

## 🔍 1. Find by Name

### Exact match

```bash
find /home -name "file.txt"
```

### Case-insensitive

```bash
find /home -iname "file.txt"
```

### Wildcards

```bash
find /home -name "*.log"
```

---

## 📁 2. Find by Type

```bash
find /path -type f   # files
find /path -type d   # directories
find /path -type l   # symbolic links
```

---

## 📏 3. Find by Size

```bash
find /path -size 10M     # exactly 10MB
find /path -size +10M    # greater than 10MB
find /path -size -10M    # less than 10MB
```

Units:

* `k` → KB
* `M` → MB
* `G` → GB

---

## ⏱️ 4. Find by Time

### Modified time

```bash
find /path -mtime 1     # modified 1 day ago
find /path -mtime -1    # modified within last 24h
```

### Access time

```bash
find /path -atime 1
```

### Change time

```bash
find /path -ctime 1
```

---

## 👤 5. Find by Owner

```bash
find /path -user username
```

---

## 🔐 6. Find by Permissions

```bash
find /path -perm 777
find /path -perm -4000   # SUID files
```

---

## 🔎 7. Find Empty Files/Directories

```bash
find /path -empty
```

---

## 🧵 8. Combine Conditions (AND / OR)

### AND (default)

```bash
find /path -name "*.log" -size +1M
```

### OR

```bash
find /path -name "*.log" -o -name "*.txt"
```

---

## ⚙️ 9. Execute Commands on Results

### Delete files

```bash
find /path -name "*.tmp" -delete
```

### Using `-exec`

```bash
find /path -name "*.log" -exec rm {} \;
```

### Using `xargs`

```bash
find /path -name "*.log" | xargs rm
```

---

## 📂 10. Find and Copy Files

```bash
find /path -name "*.txt" -exec cp {} /destination/ \;
```

---

## 🔍 11. Find Hidden Files

```bash
find /path -name ".*"
```

---

## 📉 12. Limit Search Depth

```bash
find /path -maxdepth 1
find /path -mindepth 2
```

---

## 🚫 13. Exclude Paths

```bash
find /path -path "/path/exclude" -prune -o -print
```

---

## 🔁 14. Find with Regex

```bash
find /path -regex ".*\.log"
```

---

## 🧪 15. Print / Debug Output

```bash
find /path -print
```

---

## ⚡ 16. Real-World / Pentesting Examples

### 🔍 Find large files (disk cleanup / data hunting)

```bash
find / -type f -size +100M 2>/dev/null
```

### 🔐 Find SUID files (privilege escalation)

```bash
find / -perm -4000 2>/dev/null
```

### 🧨 Find writable files (possible exploitation)

```bash
find / -writable 2>/dev/null
```

### 👑 Find files owned by root

```bash
find / -user root 2>/dev/null
```

### 🔑 Find SSH keys

```bash
find / -name "id_rsa" 2>/dev/null
```

### 🧾 Find config files

```bash
find / -name "*.conf" 2>/dev/null
```

---

## ⚠️ Tips

* Use `2>/dev/null` to hide permission errors
* Be careful with `-delete` (irreversible)
* Test commands before executing destructive actions
* Use quotes to avoid shell expansion (`"*.log"`)

---

## 🧠 Summary

The `find` command is essential for:

* File discovery
* System administration
* Automation
* Cybersecurity & privilege escalation

👉 Mastering `find` = huge boost in Linux + hacking skills 🚀
