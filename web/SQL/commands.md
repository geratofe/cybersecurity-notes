# SQL Commands (Practical Reference)

---

# 1. Database Management

```sql
CREATE DATABASE namehere;
-- Creates a new database
-- Use when setting up a new environment
```

```sql
SHOW DATABASES;
-- Lists all databases
-- Useful for enumeration
```

```sql
USE namehere;
-- Selects a database to work with
-- Required before accessing tables
```

```sql
DROP DATABASE namehere;
-- Deletes a database permanently
-- ⚠️ Dangerous: irreversible
```

---

# 2. Table Management

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username name(50),
    password passpass(100)
);
-- Creates a new table with defined columns
-- Used when designing database structure
```

```sql
SHOW TABLES;
-- Lists all tables in the current database
-- Useful for enumeration
```

```sql
DESCRIBE users;
-- Displays table structure (columns, data types)
-- Important for understanding schema
```

```sql
ALTER TABLE users ADD email namehere(100);
-- Modifies table structure
-- Used to add or change columns
```

```sql
DROP TABLE users;
-- Deletes a table permanently
-- ⚠️ Dangerous: data loss
```

---

# 3. Data Manipulation

```sql
INSERT INTO users (username, password)
VALUES ('john', '1234');
-- Adds a new row to the table
-- Used to create new records
```

```sql
SELECT * FROM users;
-- Retrieves all data from the table
-- Useful for initial inspection
```

```sql
SELECT username FROM users;
-- Retrieves specific column(s)
-- Used for targeted queries
```

```sql
UPDATE users SET password='newpass' WHERE username='john';
-- Updates existing data
-- ⚠️ Always use WHERE to avoid affecting all rows
```

```sql
DELETE FROM users WHERE username='john';
-- Deletes specific rows
-- ⚠️ Without WHERE deletes everything
```

---

# 4. Filtering & Logic

```sql
SELECT * FROM users WHERE username = 'admin';
-- Filters results based on condition
-- Essential for narrowing results
```

```sql
SELECT * FROM users WHERE id > 5;
-- Returns rows where condition is true
```

```sql
SELECT * FROM users WHERE username != 'guest';
-- Excludes matching values
```

```sql
SELECT * FROM users WHERE username='admin' AND password='1234';
-- Both conditions must be true
```

```sql
SELECT * FROM users WHERE username='admin' OR username='root';
-- At least one condition must be true
```

```sql
SELECT * FROM users WHERE NOT username='admin';
-- Negates a condition
```

---

# 5. Pattern Matching

```sql
SELECT * FROM users WHERE username LIKE 'a%';
-- Matches values starting with 'a'
```

```sql
SELECT * FROM users WHERE username LIKE '%admin%';
-- Matches values containing 'admin'
```

```sql
SELECT * FROM users WHERE username LIKE '%n';
-- Matches values ending with 'n'
```

---

# 6. Sorting & Limiting

```sql
SELECT * FROM users ORDER BY id ASC;
-- Sorts results in ascending order
```

```sql
SELECT * FROM users ORDER BY id DESC;
-- Sorts results in descending order
```

```sql
SELECT * FROM users LIMIT 5;
-- Limits number of results returned
-- Useful for large datasets
```

---

# 7. Aggregation

```sql
SELECT COUNT(*) FROM users;
-- Counts number of rows
```

```sql
SELECT SUM(id) FROM users;
-- Returns total sum
```

```sql
SELECT AVG(id) FROM users;
-- Returns average value
```

```sql
SELECT MAX(id) FROM users;
-- Returns highest value
```

```sql
SELECT MIN(id) FROM users;
-- Returns lowest value
```

---

# 8. DISTINCT

```sql
SELECT DISTINCT username FROM users;
-- Removes duplicate values
-- Useful for unique results
```

---

# 9. JOIN (Combining Tables)

```sql
SELECT users.username, orders.item
FROM users
JOIN orders ON users.id = orders.user_id;
-- Combines data from multiple tables
-- Used when data is related across tables
```

---

# 10. Enumeration (Important for SQLi)

```sql
SHOW DATABASES;
-- List databases
```

```sql
SHOW TABLES;
-- List tables
```

```sql
DESCRIBE users;
-- Show table structure
```

---

# 11. Useful Functions

```sql
SELECT database();
-- Returns current database name
```

```sql
SELECT user();
-- Returns current user
```

```sql
SELECT version();
-- Returns database version
```

---

# 12. Comments

```sql
-- comment
# comment
-- Used to ignore part of a query
-- Important in SQL injection
```

---

# ⚠️ Important Warnings

* UPDATE without WHERE → modifies all rows
* DELETE without WHERE → deletes all data
* DROP → irreversible

---

# 🧠 Summary

* DDL → CREATE, DROP, ALTER
* DML → SELECT, INSERT, UPDATE, DELETE
* Logic → WHERE, AND, OR
* Analysis → COUNT, AVG
* Enumeration → SHOW, DESCRIBE

---

# 🔥 Why This Matters

These commands are essential for:

* database management
* backend systems
* SQL injection exploitation
