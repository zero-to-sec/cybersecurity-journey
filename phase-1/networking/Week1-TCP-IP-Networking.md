# TCP/IP & Networking - Week 1 Notes

## TCP/IP Model
Similar to OSI but simpler - 4 layers only
Easier to correlate to real world

| Layer       | Protocols              |
|-------------|------------------------|
| Application | HTTP, FTP, SMTP, TLS/SSL |
| Transport   | TCP, UDP               |
| Internet    | IPv4, IPv6, ICMP, IGMP |
| Link        | ARP                    |

---

## IP Address & Subnet Mask
IP Address = 32 bits (4 groups of 8 bits)
Example: 10.0.2.15
- 10.0.2 = Network part
- 15 = Host (device) part

Subnet Mask 255.255.255.0 = /24
Means first 24 bits reserved for network
Remaining 8 bits = 256 possible hosts

Gateway = 10.0.2.1 (Router - exit door to internet)

---

## ARP (Address Resolution Protocol)
Translates IP address → MAC address
Used inside LAN only
Broadcast to find who has the IP
Example: "Who has 10.0.2.1?" → Router replies with MAC

---

## ICMP
Used by ping and traceroute
ping = sends Echo Request → gets Echo Reply
traceroute = shows every hop (router) to destination

## TTL (Time To Live)
Linux default TTL = 64
Windows default TTL = 128
Each router reduces TTL by 1
TTL = 0 → packet dropped → traceroute records that hop

---

## Kali Commands
ip addr        → show IP address and subnet mask
ip route       → show default gateway
ping -c 4 8.8.8.8     → test internet connection
ping -c 4 google.com  → test DNS + connection
traceroute google.com → show full path to destination
nslookup google.com   → query DNS server

---

## Encapsulation (Data going out)
Application → Data
Transport   → TCP header added → Segment
Internet    → IP header added  → Packet
Link        → Ethernet header  → Frame

## Decapsulation (Data coming in)
Frame → Packet → Segment → Data
Each layer removes its header
