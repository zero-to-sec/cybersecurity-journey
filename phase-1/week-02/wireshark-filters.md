# Week 2 - Day 2: Wireshark + Filters + TCP Handshake

## What is Wireshark
Free program - works on mac, windows, linux
Captures and analyzes all network traffic byte by byte
Shows: TCP, UDP, HTTP, DNS, ARP, ICMP and all protocols

## Why use Wireshark

### Network Troubleshooting
Identify misconfigurations, packet drops, protocol errors
Find if internet is cut or connection has problems

### Performance Monitoring
Analyze latency, packet loss, retransmissions, DNS time

### Security Analysis
Detect: Port Scanning, ARP Spoofing, Malware Traffic,
DNS Tunneling, suspicious connections

---

## Wireshark Filters

### Capture Filters
Applied BEFORE capture starts
Just write name of protocol filter
Example: tcp, udp, http, dns

### Display Filters
Applied AFTER capture - filter what you see
Rules: mini letters, background green = ok, red = wrong
In value field: can write capital letters

---

## IP Address Display Filters
ip.addr==(IP)         → all traffic to/from IP
ip.addr eq (IP)       → same as above
ip.addr==(IP)/24      → track full network
ip.src==(IP)          → traffic FROM this IP only
ip.dst==(IP)          → traffic TO this IP only
ip.src==(IP)/24       → from entire network
ip.dst==(IP)/24       → to entire network

---

## Logical Operators

### OR ( || )
ip.addr==(IP1) or ip.addr==(IP2)
Shows traffic between 2 IPs - condition: one must exist

### AND ( && )
ip.addr==(IP1) and ip.addr==(IP2)
Shows traffic between exactly 2 IPs bidirectional
ip.src==(IP1) && ip.addr==(IP2)
ip.src==(IP1) && ip.dst==(IP2)

### NOT ( ! )
not ip.addr==(IP1)
Shows all traffic EXCEPT from IP1
not ip.addr==(IP1) and not ip.addr==(IP2)

### OR NOT ( || ! )
ip.addr==(IP1) or not ip.addr==(IP2)
or not = wider
or not = broader

---

## Comparison Operators
== / eq     → equal
!= / ne     → not equal
> / gt      → greater than
< / lt      → less than
>= / ge     → greater than or equal
<= / le     → less than or equal

Examples:
dns.count.answers > (IP)
dns.count.answers >= (IP)
dns.count.answers < (IP)
dns.count.answers <= (IP)

Note: these show delta value - time between last packet
and this - if time is 0 it means destination is in source

To solve: not ip.addr == (ip)
But also show connection with MAC
To resolve: and not arp (protocol)

---

## Other Operators

### Contains
dns.contains "wireshark"
udp.contains "wireshark"
tcp contains "mail"

### Matches (regex)
dns.matches "(?)mp3"
dns.matches "(?)mp2"
dns.matches "(?)mp3"

---

## Port Display Filters
web: tcp.port == 80
registered ports: tcp.port == 41352
tcp.port >= 20

---

## Pentesting Use Cases in Wireshark
tcp contains "username"
tcp contains "pass"
tcp contains "ticket"
http contains "password"
http contains "admin"
dns contains "google"

---

## MAC Address Filters
eth.addr==(MAC) → all traffic to/from MAC
eth.src==(MAC)  → from this MAC
eth.dst==(MAC)  → to this MAC
eth.addr==(MAC) and eth.addr==(MAC)
→ show connection from source MAC direction

---

## How to Build Display Filter
A: specially for IPv4
AAAA: specially for IPv6

---

## TCP Three-Way Handshake
Before sending data, two devices do handshake
To confirm they know each other and ready to transfer

Step 1: SYN     → Client sends: "I want to connect"
Step 2: SYN-ACK → Server responds: "Ok, I confirm"
Step 3: ACK     → Client confirms: "Connection established"

After this: data transfer begins

---

## Bandit Level 3
Challenge: hidden file inside inhere folder
Commands used:
cd inhere
ls -la
cat .hidden
Lesson: hidden files in Linux start with dot (.)
ls -la shows hidden files, ls alone does not
