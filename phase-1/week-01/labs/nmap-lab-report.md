# Nmap Lab Report

**Date:** 2026-10-27
**Target:** 192.168.56.101 (VirtualBox VM, Host-Only network)
**Authorization:** My own VM on my own machine

## Commands Used
```
nmap -sS 192.168.56.101
nmap -sV 192.168.56.101
nmap -p- 192.168.56.101
```

## Scan 1: Before starting a service

### Raw output (-sS)
```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 12:24 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0025s latency).
All 1000 scanned ports on 192.168.56.101 are in ignored states.
Not shown: 1000 closed tcp ports (reset)
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)
```

### Raw output (-p-)
```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 12:28 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0021s latency).
All 65535 scanned ports on 192.168.56.101 are in ignored states.
Not shown: 65535 closed tcp ports (reset)
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)
```

### My interpretation (line by line)
- **Host is up (0.0025s latency):** it simply means that the device respond
- **1000 closed tcp ports (reset):** this means the RST system is correct
- **MAC Address 08:00:27:8A:35:D2:** this means that the advice I am testing is on the same local network
- **Difference between -sS and -sV:** -sS sends a half scan (only SYN), but -sV makes a full connection with the server to find the state, service and version.
- **What -p- did differently:** TODO (how many ports did it scan, and what was the result?)

## Scan 2: After starting a service (port 8000)

### Raw output (-sS)
```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 12:31 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0018s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
8000/tcp open  http-alt
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)
```

### Raw output (-sV)
```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 13:17 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0027s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
8000/tcp open  http    SimpleHTTPServer 0.6 (Python 3.13.12)
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)
```

### My interpretation
- **PORT:** 8000/tcp
- **STATE:** open
- **SERVICE:** http-alt in the -sS scan, but http in the -sV scan. TODO (why do you think they are different?)
- **VERSION:** SimpleHTTPServer 0.6 (Python 3.13.12), the program name and its version.

## Before vs After
Before the service existed, all ports were closed and no results appeared. After the service existed, port 8000 became open. because python -m http.server opened port 8000 to listen

## What I didn't understand and how I found the answer
- **Question:** What does "alt" mean in http-alt?
- **Answer:** It is short for "alternative". The standard port for HTTP is 80, so any web server running on another port such as 8000, 8080 or 8888 is called http-alt by nmap.
