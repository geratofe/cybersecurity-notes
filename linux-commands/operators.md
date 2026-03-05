# Linux Command Operators

This file explains **common shell operators** used with Linux commands, including **command chaining, output redirection, and error handling**.  
These operators are extremely useful for **automation, logging, and pentesting**.

---

## 1️⃣ The `&&` Operator

**Purpose:** Run the next command **only if the previous one succeeds**.

**Syntax:**

```bash
command1 && command2
```

**Examples:**

- Print messages in sequence:

```bash
echo "Hello" && echo "World"
```

- Create a folder and enter it:

```bash
mkdir test_folder && cd test_folder
```

- Git workflow:

```bash
git add . && git commit -m "Updated notes" && git push
```

**Pentesting Use Example:**

```bash
find / -type f -perm -4000 2>/dev/null && echo "Found SUID files"
```

- Only prints `"Found SUID files"` if `find` succeeds.

---

## 2️⃣ The `>>` Operator

**Purpose:** Append the output of a command to a file.

- If the file doesn’t exist → it is created  
- If the file exists → output is added to the end  

**Syntax:**

```bash
command >> file.txt
```

**Examples:**

- Append a message:

```bash
echo "New entry" >> notes.txt
```

- Save `ls` output:

```bash
ls >> file_list.txt
```

- Save `find` results:

```bash
find / -type f -name "*.conf" 2>/dev/null >> config_files.txt
```

**Pentesting Use Example:**

```bash
grep -Ri "password" / 2>/dev/null >> potential_passwords.txt
```

- Collects all matches for `"password"` into one file.

---

## 3️⃣ The `>` Operator

**Purpose:** Redirect command output to a file, **overwriting existing content**.

```bash
echo "Fresh start" > log.txt
```

- Replaces previous content with `"Fresh start"`

---

## 4️⃣ The `|` (Pipe) Operator

**Purpose:** Send the output of one command as input to another.

```bash
command1 | command2
```

**Examples:**

- Search within `find` results:

```bash
find / -type f -name "*.log" 2>/dev/null | grep "error"
```

- Count lines containing a word:

```bash
grep "failed" auth.log | wc -l
```

---

## 5️⃣ `2>/dev/null` (Error Redirection)

**Purpose:** Hide error messages, usually **“Permission denied”**.

**Example:**

```bash
find / -type f -name "*.conf" 2>/dev/null
```

- Errors are discarded, only **useful output is displayed**

**Combining operators in pentesting:**

```bash
find / -type f -name "*.txt" 2>/dev/null >> files.txt && grep -i "password" files.txt >> passwords.txt
```

- Collects all `.txt` files → appends to `files.txt`  
- Searches for `"password"` → appends matches to `passwords.txt`

---

# Summary Table

| Operator | Purpose | Example |
|----------|---------|---------|
| `&&` | Run next command only if previous succeeds | `mkdir test && cd test` |
| `>>` | Append output to a file | `echo "log" >> output.txt` |
| `>` | Overwrite output to a file | `echo "fresh" > file.txt` |
| `|` | Send output to another command | `grep "error" log.txt | wc -l` |
| `2>/dev/null` | Hide error messages | `find / -type f 2>/dev/null` |

---

💡 **Tip:**  
These operators are **commonly combined** in pentesting scripts and Linux workflows for **automation, enumeration, and logging**.
