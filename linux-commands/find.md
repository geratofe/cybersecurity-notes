# find command

The find command searches for files and directories in a filesystem.

Basic syntax:

find [path] [options]


## Search for files

find /home -type f

-type f tells find to search for files only.


## Search for directories

find /home -type d

-type d tells find to search for directories only.


## Search by name

find /home -type f -name "notes.txt"

This searches for a file named notes.txt.


## Search for a specific extension

find /home -type f -name "*.txt"

This finds all .txt files.


## Search by file size

find / -type f -size +100M

+100M means files larger than 100 MB.

Examples:
-size +10M  (larger than 10MB)  
-size -10M  (smaller than 10MB)  
-size 10M   (exact size)


## Search by date

find / -type f -newermt 2024-01-01

This finds files modified after January 1, 2024.


## Search between dates

find / -type f -newermt 2024-01-01 ! -newermt 2024-02-01

This finds files modified between:

2024-01-01 and 2024-02-01


## Suppress permission errors

find / -type f -name "*.log" 2>/dev/null


### What does 2>/dev/null mean?

When searching the entire system, many directories require special permissions.  
If you do not have permission, Linux prints errors like:

Permission denied


### Breaking it down

2 = stderr (error output)

\> = redirect output

/dev/null = a special file that discards anything sent to it


### Why we use it

When running find on large directories like `/`, many permission errors appear and clutter the output.

Using:

find / -type f -name "*.log" 2>/dev/null

hides those error messages so you only see the results of the search.


### Example in cybersecurity enumeration

find / -type f -name "password.txt" 2>/dev/null
