# Week 1 - Day 7: Bandit CTF + Week End Assessment

## SSH Protocol
Secure Shell - encrypted connection to remote Linux server
Syntax: ssh username@hostname -p port
Example: ssh bandit0@bandit.labs.overthewire.org -p 2220

Key points:
- Password does not show when typing = normal in Linux
- Type "yes" on first connection (fingerprint verification)
- exit → returns to Kali
- Default SSH port = 22, Bandit uses 2220

---

## OverTheWire Bandit

### Level 0
Goal: connect to server and read readme file
Commands used:
ssh bandit0@bandit.labs.overthewire.org -p 2220
ls
cat readme
Result: found password for Level 1

### Level 1
Challenge: file named "-" (special character in Linux)
Problem: cat - does not work (Linux reads - as stdin)
Solution: cat ./-
Lesson: in Linux, ./ means "current directory"
Always use ./ before files with special names

---

## Week 1 - Final Assessment Results
Score: 14.5 / 15

Topics tested:
- OSI Model 7 layers: PASS
- TCP/IP and IP addressing: PASS
- DNS and HTTP/HTTPS: PASS
- Linux commands (12 commands): PASS
- Permissions and chmod: PASS
- Gateway, DHCP, ARP: PASS

---

## Week 1 Complete - Ready for Week 2
