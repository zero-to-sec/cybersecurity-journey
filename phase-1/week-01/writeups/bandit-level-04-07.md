# OverTheWire Bandit: Writeups (Level 4 → 7)

## Summary

| Level | Goal | Key Command | Result |
|---|---|---|---|
| 4 → 5 | The only human-readable file | `file ./-*` then `cat ./-file07` | `inhere/-file07` |
| 5 → 6 | 1033 bytes, not executable | `find . -type f -size 1033c ! -executable` | `inhere/maybehere07/.file2` |
| 6 → 7 | Owned by bandit7, group bandit6, 33 bytes | `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null` | `/var/lib/dpkg/info/bandit7.password` |

---

## Level 4 → 5

**Goal:** The password is stored in the only human-readable file in the `inhere` directory.

**Commands:**

```bash
ls
cd inhere
ls -la
cat ./-file07
```

**Why these commands:**

- `ls -la` lists all files with permissions and sizes. There are 10 files (`-file00` to `-file09`), all 33 bytes.
- The filenames start with a dash (`-`). If you run `cat -file07`, `cat` treats it as an **option**, not a filename. Prefixing `./` makes it an explicit path: `cat ./-file07`.
- Opening `-file00` printed garbage characters, because it is **binary data**. Only `-file07` contained readable text.

**Mistakes and lessons:**

- `cat ./'file00'` failed with "No such file" because the real name is `-file00`.
- Opening files one by one fills the terminal with binary junk. A better approach:

```bash
file ./-*
```

`file` identifies each file's type, and only `-file07` shows as `ASCII text`.

**Password (bandit5):** `********************`

---

## Level 5 → 6

**Goal:** Find a file inside `inhere` (which has 20 subdirectories, `maybehere00` to `maybehere19`) that is human-readable, 1033 bytes in size, and not executable.

**Commands (in order, including failed attempts):**

```bash
find /inhere -size 1033k -perm 640     # failed
find -size 1033k -perm 640             # no result
find -size 1033c -perm 640             # ./maybehere07/.file2
cat ./maybehere07/.file2
```

**Why:**

- `find` searches all subdirectories at once, instead of entering 20 folders manually.
- `-size 1033c`: the `c` suffix means **bytes**. `k` means kilobytes (rounded up), which is why `1033k` returned nothing. **The unit matters.**
- `/inhere` failed because the real directory is `~/inhere`, not `/inhere` at the filesystem root. Use `.` for the current directory.
- `-perm 640` (`rw-r-----`) matched because the file is not executable and has exactly these permissions.
- `-perm -x` returned `invalid mode`. `-perm` expects a numeric or symbolic mode (like `u+x`), not `-x`.
- The file is `.file2`, a **hidden file** (starts with a dot). It does not show in plain `ls`, so `ls -la` or `find` is needed.

**Better command (no guessing permissions):**

```bash
find . -type f -size 1033c ! -executable
```

`! -executable` directly means "not executable".

**Password (bandit6):** `**********************`

---

## Level 6 → 7

**Goal:** Find a file somewhere on the server that is owned by user `bandit7`, group `bandit6`, and 33 bytes in size.

**Commands:**

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
```

**Breakdown:**

| Part | Meaning |
|---|---|
| `find /` | Search the entire filesystem |
| `-type f` | Regular files only |
| `-user bandit7` | Owner is bandit7 |
| `-group bandit6` | Group is bandit6 |
| `-size 33c` | Size is 33 bytes |
| `2>/dev/null` | Discard error messages (stderr) |

**Why `2>/dev/null`?**

Searching from `/` goes through many directories you cannot access, which produces hundreds of `Permission denied` lines that bury the real result. Those messages go to **stderr (file descriptor 2)**, while the matching file goes to **stdout (1)**. `2>/dev/null` sends stderr to the "trash" and leaves only the result on screen.

**Experiments and mistakes:**

- With `1>/dev/null`, only the errors appeared: it hides stdout (the result) and leaves stderr visible.
- In my last attempt I wrote `... -size 33c /dev/null` without `2>`. `find` treated `/dev/null` as a search path, not a redirection, and returned `paths must precede expression`. A redirection needs `2>`, not just a space.

**Password (bandit7):** `*******************`

---

## Takeaways

1. A filename starting with `-`: prefix it with `./`.
2. Use `file` to identify a file's type before running `cat` on it.
3. `-size` units: `c` = bytes, `k` = kilobytes.
4. Hidden files start with a dot; use `ls -la`.
5. `find` combines conditions (`-user`, `-group`, `-size`, `-type`) and solves most of these challenges.
6. `2>/dev/null` hides errors only, never the results.
