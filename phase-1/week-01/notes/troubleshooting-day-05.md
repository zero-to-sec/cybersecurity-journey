# Troubleshooting Log: Day 5 (2026-11-10)

Every problem I hit while learning Linux commands today, why it happened, and how I fixed it.

- **Part A:** OverTheWire Bandit, Levels 4 → 7
- **Part B:** Linux one-liners on Kali

## Quick Reference

| # | Part | Problem | Root Cause | Fix |
|---|---|---|---|---|
| 1 | Bandit 4 | `No such file or directory` | Dropped the leading `-` from the filename | Copy the exact name from `ls -la` |
| 2 | Bandit 4 | Terminal full of garbage characters | Opened binary files with `cat` | `file ./-*` first, `reset` if broken |
| 3 | Bandit 5 | `find: '/inhere': No such file or directory` | Absolute path instead of relative | Use `.` |
| 4 | Bandit 5 | `-size 1033k` returned nothing | `k` = kilobytes, not bytes | Use `1033c` |
| 5 | Bandit 5 | `find: invalid mode '-x'` | Wrong `-perm` syntax | Use `! -executable` |
| 6 | Bandit 6 | Hundreds of `Permission denied` lines | `find /` scans unreadable directories | `2>/dev/null` |
| 7 | Bandit 6 | `1>/dev/null` showed only errors | `1` = stdout (results), not stderr | Use `2>` |
| 8 | Bandit 6 | `paths must precede expression` | Wrote `/dev/null` without `2>` | `2>/dev/null` |
| 9 | One-liner 3 | `zsh: permission denied: ./hello` | Mode 644 has no execute bit | `chmod 755 hello` |
| 10 | One-liner 4 | `cat: hello: Permission denied` | Mode 222 has no read bit | `chmod 644 hello` |
| 11 | One-liner 2 | Wrong order when sorting `%MEM` | `sort` without `-n` sorts as text | `sort -k4 -n -r` |
| 12 | One-liner 2 | Header line appears in the sort | Header is text, counts as 0 | Expected: it goes to the bottom, `head` cuts it |
| 13 | One-liner 1 | `*.conf` can break `find` | Shell expands `*` before `find` runs | Quote it: `"*.conf"` |
| 14 | One-liner 1 | `Permission denied` still printed with a pipe | stderr does not travel through `\|` | `2>/dev/null` before the pipe |

---

# Part A: Bandit Levels 4 → 7

## Problem 1: `No such file or directory` (Level 4)

**Command:** `cat ./'file00'`
**Error:** `cat: ./file00: No such file or directory`

**Cause:** The real filename is `-file00`. I dropped the leading dash.

**Solution:**

```bash
cat ./-file00
```

**Lesson:** A name starting with `-` is read as an option. `./` makes it an explicit path, and the dash is part of the name.

---

## Problem 2: Garbage characters in the terminal (Level 4)

**Symptom:** After `cat ./-file00`, the screen showed `�` symbols and the prompt got mixed into the output.

**Cause:** The file is binary data. `cat` sends raw bytes and the terminal tries to interpret them as characters and control codes.

**Solution:**

```bash
file ./-*      # only -file07 is "ASCII text"
reset          # if the terminal is already corrupted
```

**Lesson:** Run `file` before `cat` on unknown files.

---

## Problem 3: Wrong search path (Level 5)

**Command:** `find /inhere -size 1033k -perm 640`
**Error:** `find: '/inhere': No such file or directory`

**Cause:** `/inhere` is a directory at the filesystem root. The real one is `~/inhere`.

**Solution:** I was already inside it, so use `.`:

```bash
find . -size 1033c
```

**Lesson:** Leading `/` = absolute path from root. `.` = current directory.

---

## Problem 4: Wrong size unit (Level 5)

**Command:** `find -size 1033k -perm 640` (no output)

**Cause:** `k` means kilobytes (rounded up). The challenge gave bytes.

| Suffix | Unit |
|---|---|
| `c` | bytes |
| `k` | kilobytes |
| `M` | megabytes |

**Solution:** `find . -size 1033c`

**Lesson:** The unit matters.

---

## Problem 5: Invalid permission mode (Level 5)

**Command:** `find -size 1033c -perm -x`
**Error:** `find: invalid mode '-x'`

**Cause:** `-perm` needs a numeric mode (`640`) or symbolic mode (`u+x`). Bare `-x` is invalid. My next guess, `-perm 740`, matched nothing because I was guessing.

**Solution:**

```bash
find . -type f -size 1033c ! -executable
```

**Note:** The file was `./maybehere07/.file2`, a hidden file (starts with a dot), so plain `ls` would not show it.

**Lesson:** Use `! -executable` instead of guessing numbers. Use `ls -la` for hidden files.

---

## Problem 6: Flood of `Permission denied` (Level 6)

**Command:** `find / -type f -user bandit7 -group bandit6 -size 33c`

**Symptom:** The real result was buried under hundreds of lines like `find: '/root': Permission denied`.

**Cause:** Searching from `/` goes through directories I cannot read. Errors go to **stderr (2)**; matches go to **stdout (1)**.

**Solution:**

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

**Lesson:** `2>/dev/null` hides errors only, never results.

---

## Problem 7: Confusing `1>` and `2>` (Level 6)

**Experiment:** `1>/dev/null` showed the errors on screen.

**Cause:** Correct behaviour. `1>/dev/null` hides stdout (the results) and leaves stderr visible, the opposite of what I wanted.

| Syntax | Effect |
|---|---|
| `>` or `1>` | Redirect stdout |
| `2>` | Redirect stderr |
| `2>&1` | Send stderr to the same place as stdout |
| `>/dev/null 2>&1` | Hide everything |

---

## Problem 8: `paths must precede expression` (Level 6)

**Command:** `find / -type f -user bandit7 -group bandit6 -size 33c /dev/null`

**Error:**

```
find: paths must precede expression: `/dev/null'
find: possible unquoted pattern after predicate `-size'?
```

**Cause:** I forgot `2>`. Without it, `find` reads `/dev/null` as a second search path placed after the expression.

**Solution:** `... -size 33c 2>/dev/null`

**Lesson:** `/dev/null` alone is a path. `2>/dev/null` is a redirection.

---

# Part B: Linux One-Liners on Kali

## Problem 9: `permission denied` when running a file (One-liner 3)

**Commands:**

```bash
echo 'echo hello' > hello
chmod 644 hello
./hello
```

**Error:** `zsh: permission denied: ./hello`

**Cause:** 644 = `rw-r--r--`. There is no `x` bit anywhere, so the file can be read but not executed.

**Solution:**

```bash
chmod 755 hello
./hello          # prints: hello
```

**Lesson:** Reading (`cat`) needs `r`. Running (`./hello`) needs `x`. Numbers: r = 4, w = 2, x = 1.

| Mode | Symbolic | `./hello` | `cat ./hello` |
|---|---|---|---|
| 644 | `rw-r--r--` | permission denied | works |
| 755 | `rwxr-xr-x` | works | works |

---

## Problem 10: Cannot read my own file (One-liner 4)

**Commands:**

```bash
chmod 222 hello
cat hello
```

**Error:** `cat: hello: Permission denied`

**Cause:** 222 = `-w--w--w-`. Write only, no read bit. Even the owner cannot read the file without `r`.

**Solution:**

```bash
chmod 644 hello
```

**Lesson:** Permissions apply to the owner too. The owner is not automatically allowed to do everything.

---

## Problem 11: Wrong sort order (One-liner 2)

**Command:** `ps aux | sort -k4 -r | head -5` (without `-n`)

**Symptom:** `9.1` ranked above `10.5`.

**Cause:** Without `-n`, `sort` compares text character by character, and `"9"` comes after `"1"`.

**Solution:**

```bash
ps aux | sort -k4 -n -r | head -5
```

| Flag | Meaning |
|---|---|
| `-k4` | Sort by column 4 (`%MEM`) |
| `-n` | Numeric sort |
| `-r` | Reverse (largest first) |

**Lesson:** Always add `-n` when sorting numbers.

---

## Problem 12: The header line in `ps aux` (One-liner 2)

**Observation:** `ps aux` prints a header line (`USER PID %CPU %MEM ...`) that is not data.

**Cause:** The header is text, so with `-n` it counts as 0 and goes to the bottom with `-r`. Since `head -5` only keeps the top 5, it never shows up in the result.

**Lesson:** Know what is in your input. If I used `tail` instead of `head`, the header would appear.

---

## Problem 13: Unquoted `*.conf` (One-liner 1)

**Command:** `find /etc -name *.conf`

**Risk:** The shell expands `*` before `find` runs. If `.conf` files exist in the current directory, `find` receives several filenames instead of one pattern and fails with the same error as Problem 8: `paths must precede expression`.

**Solution:** Quote the pattern so `find` receives it untouched:

```bash
find /etc -name "*.conf"
```

**Lesson:** Quote wildcards you want `find` to interpret, not the shell.

---

## Problem 14: Errors bypass the pipe (One-liner 1)

**Command:** `find /etc -name "*.conf" -printf "%s %p\n" | sort -n -r | head`

**Symptom:** `Permission denied` messages still appeared on screen, mixed into the output.

**Cause:** A pipe (`|`) only carries **stdout**. Errors go to **stderr**, which skips the pipe and prints straight to the terminal.

**Solution:** Redirect stderr on the command that produces it, before the pipe:

```bash
find /etc -name "*.conf" -printf "%s %p\n" 2>/dev/null | sort -n -r | head
```

**Lesson:** `2>` belongs right after the command that generates the errors.

| Part | Meaning |
|---|---|
| `-printf "%s %p\n"` | Print size in bytes, then path, then newline |
| `sort -n -r` | Numeric, largest first |
| `head` | Keep the first 10 lines |

---

# Commands of the Day

| Command | Purpose |
|---|---|
| `ls -la` | List all files (including hidden) with permissions |
| `cat ./-file` | Read a file whose name starts with `-` |
| `file ./-*` | Identify file types before opening |
| `find . -type f -size 1033c ! -executable` | Find by size, not executable |
| `find / -type f -user X -group Y -size 33c 2>/dev/null` | Find by owner, group, size; hide errors |
| `find /etc -name "*.conf" -printf "%s %p\n" 2>/dev/null \| sort -n -r \| head` | Largest `.conf` files |
| `ps aux \| sort -k4 -n -r \| head -5` | Top 5 processes by memory |
| `chmod 644 / 755 / 222 file` | Change permissions |
| `2>/dev/null` | Discard errors |
| `reset` | Repair a corrupted terminal |

# Final Takeaways

1. Read the error message first. Most errors above said exactly what was wrong.
2. Run `file` before `cat` on unknown files.
3. Check units (`-size c` vs `k`) and flags (`sort -n`).
4. Prefer `! -executable` over guessing permission numbers.
5. Quote wildcards you want a command to interpret (`"*.conf"`).
6. Pipes carry stdout only. Redirect stderr with `2>` before the pipe.
7. `r` is needed to read, `x` is needed to run, even for the file's owner.
8. Copy passwords from the terminal instead of retyping them (`l`, `I`, `1`, `0`, `O` look alike).
