# Linux One-Liners 🐧

## 1) chmod: Change permissions
```bash
chmod 754 script.sh
```
**Explanation:** The numbers = r(4) + w(2) + x(1).
Owner gets 7 (read+write+execute), group gets 5 (read+execute), others get 4 (read only).

## 2) awk: Print a column from a delimited file
```bash
awk -F: '{print $1}' /etc/passwd
```
**Explanation:** The passwd file is separated by `:` instead of spaces, so I set the delimiter with `-F:` and print the first column (usernames).

## 3) grep + awk: Filter, then extract
```bash
grep "root" /etc/passwd | awk -F: '{print $1, $NF}'
```
**Explanation:** `grep` selects the lines containing "root", and `awk` prints the first column and the last column (`$NF`).

## 4) awk: Change the content of a column
```bash
awk '{$3="Expert"; print $0}' file.txt
```
**Explanation:** Replaces column 3 with the word "Expert" and prints the whole line (`$0`).

## 5) awk + sort: Extract, then sort
```bash
awk '{print $1, $2}' file.txt | sort -k2
```
**Explanation:** Prints the first two columns, then `sort -k2` sorts them by the second column.
