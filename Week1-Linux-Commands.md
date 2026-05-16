# Linux Commands - Week 1 Notes

## pwd - Print Working Directory
Shows current location in the system
Example: /home/kali

## ls - List
Shows files and folders in current directory
ls          → simple list
ls -la      → detailed list (permissions, size, date)
ls -a       → show hidden files
ls -l       → long format
ls -t       → sort by time
ls -7       → combine options

## cd - Change Directory
Navigate between folders
cd Documents          → Relative Path (from current location)
cd /home/kali/Documents → Absolute Path (full path)
cd ..                 → go back one folder
cd ~                  → go to home folder

## mkdir - Make Directory
Creates a new folder
mkdir HackerLab       → create one folder
mkdir -p Projects/Linux/Basics → create full path at once

## touch - Create File
Creates a new empty file
touch notes.txt
If file exists → updates timestamp only
Use ls -l to verify (size = 0 means empty)

## cat - Concatenate
Reads and displays file content in terminal
cat notes.txt         → display content
cat -n notes.txt      → display with line numbers
cat > notes.txt       → create file and write (CTRL+D to save)
Works best with: text files, scripts, config files, logs
Warning: do not use cat with large files

## cp - Copy
Copies file or folder to another location
cp notes.txt backup.txt     → copy file
cp -r Projects Backup       → copy folder recursively
cp -f                       → force copy (overwrite)
cp -p                       → keep original permissions
cp -v                       → show what is being copied
cp -i                       → ask before overwrite
Cybersecurity use: copying logs for analysis without changing timestamps

## mv - Move / Rename
Moves file or renames it
mv file folder/             → move file
mv old new                  → rename file
mv -i                       → ask before overwrite
mv -v                       → show what is moving
mv -b                       → create backup before overwrite

## rm - Remove
Deletes files and folders
rm file                     → delete file
rm -r folder                → delete folder recursively
rm -f                       → force delete no warning
rm -i                       → ask before delete
Warning: no recycle bin in Linux - deleted forever

## echo - Print / Write to File
Prints text or writes to file
echo "Hello"                → print to terminal
echo "Hello" >> notes.txt   → append to file (keeps existing content)
echo "Hello" > notes.txt    → overwrite file

## grep - Search Inside File
Searches for a word inside a file
grep "OSI" notes.txt        → find OSI in file
grep -i "osi" notes.txt     → case insensitive search

## find - Search for Files
Searches for files by name
find /home -name "notes.txt"   → find specific file
find /home -name "*.txt"       → find all .txt files
find / -name "notes.txt"       → search entire system

---

## Kali Practice Commands
pwd
ls -la
mkdir ~/HackerLab
cd ~/HackerLab
touch notes.txt
echo "OSI has 7 layers" >> notes.txt
echo "DNS resolves names to IPs" >> notes.txt
cat notes.txt
cat -n notes.txt
grep "OSI" ~/HackerLab/notes.txt
find /home -name "*.txt"
