# grep Command

`grep` is used to search for specific words or patterns inside files.

It prints lines that match the search pattern.

The name comes from:

Global Regular Expression Print

---

# Basic Usage

Basic syntax:

```bash
grep [options] pattern file
```

Example:

```bash
grep "admin" users.txt
```

This searches for the word **admin** inside `users.txt`.

---

# Filters

## Case insensitive search

```bash
grep -i "admin" users.txt
```

`-i` ignores uppercase and lowercase differences.

Example matches:

admin  
Admin  
ADMIN  

---

## Search recursively in directories

```bash
grep -r "password" /home
```

Searches inside **all files in a directory**.

---

## Show line numbers

```bash
grep -n "error" log.txt
```

Shows the **line number** where the match occurs.

---

## Show only filenames

```bash
grep -l "admin" *
```

Shows only files containing the word.

---

## Invert match

```bash
grep -v "root" users.txt
```

Shows lines that **DO NOT contain** the word.

---

## Count matches

```bash
grep -c "error" log.txt
```

Counts how many times the word appears.

---

# Examples

Search for errors in a log file:

```bash
grep "error" server.log
```

Search ignoring case:

```bash
grep -i "password" notes.txt
```

Search recursively in directories:

```bash
grep -r "admin" /var
```

Search and show line numbers:

```bash
grep -n "failed" auth.log
```

---

# Pentesting Uses

During penetration testing, `grep` is used to quickly search large files for sensitive information.

---

## Find passwords in files

```bash
grep -i "password" config.txt
```

Attackers search config files for credentials.

---

## Search logs for login attempts

```bash
grep "failed" auth.log
```

Useful for identifying **failed login attempts**.

---

## Search entire directories for credentials

```bash
grep -r "password" /var/www
```

Web directories sometimes contain **hardcoded passwords**.

---

## Search for API keys or tokens

```bash
grep -ri "api" .
```

Searches recursively in the current directory.

---

## Combine with other commands

Example with `find`:

```bash
find / -type f -name "*.log" 2>/dev/null | grep "error"
```

This finds log files and searches them for errors.

---

# Why grep is powerful

`grep` is powerful because it can:

- search huge files quickly
- filter command output
- find credentials
- analyze logs
- search entire systems

It is one of the most used commands in Linux system administration and penetration testing.
