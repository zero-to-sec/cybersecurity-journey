# Linux One-Liners (Applied on Kali)

Every command below was run on my own Kali machine. The results are real output, not copied.

---

## 1) Find all `.conf` files in `/etc`, sorted by size (largest first)

```bash
find /etc -name "*.conf" -printf "%s %p\n" 2>/dev/null | sort -n -r | head
```

**Result:**
```
836792 /etc/netsniff-ng/oui.conf
117149 /etc/john/john.conf
43704 /etc/legion.conf
41640 /etc/inetsim/inetsim.conf
40005 /etc/firebird/4.0/firebird.conf
32761 /etc/postgresql/18/main/postgresql.conf
29180 /etc/openal/alsoft.conf
22777 /etc/sqlmap/sqlmap.conf
15982 /etc/netsniff-ng/tcp.conf
15695 /etc/gnome-system-tools/user-profiles.conf
```

**Why it works:**
- `find /etc -name "*.conf"` finds every file ending in `.conf` (quotes stop the shell from expanding `*`).
- `-printf "%s %p\n"` prints the size in bytes (`%s`), then the path (`%p`), then a new line.
- `2>/dev/null` hides "Permission denied" errors (they go to stderr, not through the pipe).
- `sort -n -r` sorts numerically (`-n`) and in reverse (`-r`), so the biggest is first.
- `head` keeps only the first 10 lines.

---

## 2) Top 5 processes by memory usage

```bash
ps aux | sort -k4 -n -r | head -5
```

**Result (USER, PID, %CPU, %MEM, COMMAND):**
```
root   698   2.2  8.8  /usr/lib/xorg/Xorg
kali   1118  0.8  6.9  xfwm4
kali   1898  0.2  3.5  /usr/bin/qterminal
kali   1183  0.1  3.3  xfdesktop
kali   1494  0.0  3.1  /usr/bin/python3
```

**Why it works:**
- `ps aux` lists all processes of all users with details.
- Column 4 is `%MEM`, so `sort -k4` sorts by that column.
- `-n` makes it numeric (so `10.5` is bigger than `9.1`), `-r` puts the largest first.
- The header line is text, so with `-n` it counts as 0 and goes to the bottom.
- `head -5` keeps the top 5.

---

## 3) Permissions: read vs execute (644 vs 755)

```bash
echo 'echo hello' > hello
chmod 644 hello
./hello
cat ./hello
chmod 755 hello
./hello
```

**Result:**

| Permission | `./hello` | `cat ./hello` |
|---|---|---|
| 644 (`rw-r--r--`) | `zsh: permission denied: ./hello` | `echo hello` |
| 755 (`rwxr-xr-x`) | `hello` | `echo hello` |

**Why it works:**
- Numbers: r = 4, w = 2, x = 1.
- 644 = 6 (4+2) for owner, 4 for group, 4 for others. There is **no x** anywhere, so the file can be read but not executed.
- 755 = 7 (4+2+1) for owner, 5 (4+1) for group and others. The **1** adds execute permission.
- Reading (`cat`) needs `r`. Running (`./hello`) needs `x`.

---

## 4) Bonus: write-only permission (222)

```bash
chmod 222 hello
cat hello
```

**Result:**
```
cat: hello: Permission denied
```

**Why it works:**
- 222 = `-w--w--w-`: write only, no read bit (4).
- Even the owner cannot read the file without `r`.
