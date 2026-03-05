# find Command

The `find` command in Linux is used to search for files and directories based on different conditions such as name, size, type, or modification date.

It is commonly used during system administration and penetration testing to locate files quickly.

---

# Basic Usage

Basic syntax:

```bash
find [path] [options] [expression]
```

Example:

```bash
find /home -name "notes.txt"
```

This searches the `/home` directory for a file named `notes.txt`.

Example searching current directory:

```bash
find . -name "password.txt"
```

`.` means the **current directory**.

---

# Filters

Filters allow you to narrow down search results.

## Search for files

```bash
find / -type f
```

`-type f` searches **only for files**.

---

## Search for directories

```bash
find / -type d
```

`-type d` searches **only for directories**.

---

## Search by name

```bash
find / -name "notes.txt"
```

Searches for a file with the exact name.

Wildcard example:

```bash
find / -name "*.log"
```

Finds all `.log` files.

---

## Search by size

```bash
find / -size +100M
```

Finds files **larger than 100MB**.

Examples:

```bash
find / -size +50M
find / -size -10M
```

`+` means larger than  
`-` means smaller than

---

## Search by date

```bash
find / -newermt "2024-01-01"
```

Finds files modified **after a specific date**.

Date range example:

```bash
find / -newermt "2024-01-01" ! -newermt "2024-02-01"
```

Finds files modified **between January 1 and February 1**.

---

# Examples

Search for a specific file:

```bash
find / -name "password.txt"
```

Search for log files:

```bash
find /var -type f -name "*.log"
```

Search for files larger than 50MB:

```bash
find / -type f -size +50M
```

Search inside current directory:

```bash
find . -type f -name "*.txt"
```

---

# Pentesting Uses

During penetration testing, the `find` command is often used to locate sensitive files, misconfigurations, and privilege escalation opportunities.

---

## Find SUID files (Privilege Escalation)

```bash
find / -type f -perm -4000 2>/dev/null
```

Explanation:

- `-perm -4000` finds files with the **SUID bit set**
- SUID files run with the **owner's privileges**
- If owned by root, they may allow **privilege escalation**

---

## Find writable directories

```bash
find / -type d -writable 2>/dev/null
```

Explanation:

Shows directories where the current user has **write permissions**.

Attackers may use these directories to place files or scripts.

---

## Find SSH private keys

```bash
find / -type f -name "id_rsa" 2>/dev/null
```

Explanation:

`id_rsa` files are **SSH private keys**.  
If readable, they may allow access to other machines.

---

## Find configuration files

```bash
find / -type f -name "*.conf" 2>/dev/null
```

Explanation:

Configuration files sometimes contain:

- passwords
- database credentials
- API keys
- service configurations

---

## Find large files (possible backups)

```bash
find / -type f -size +100M 2>/dev/null
```

Explanation:

Large files may contain:

- backups
- databases
- logs with sensitive information

---

## Find files owned by a specific user

```bash
find / -user root 2>/dev/null
```

Example:

```bash
find / -user www-data 2>/dev/null
```

This shows files owned by a specific user.

---

# Why we use 2>/dev/null

Example:

```bash
find / -type f -name "*.log" 2>/dev/null
```

Explanation:

`2>` redirects **errors**.

`/dev/null` is a special location that discards output.

So `2>/dev/null` hides errors such as:

```
Permission denied
```

This keeps the output clean and only shows useful results.
