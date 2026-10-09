# Week 2 - Day 1: IP Address + Subnetting + CIDR

## IP Address Classes
| Class | Range | Default Mask | Used For |
|-------|-------|--------------|----------|
| A | 1-126 | 255.0.0.0 /8 | Large organizations |
| B | 128-191 | 255.255.0.0 /16 | Medium organizations |
| C | 192-223 | 255.255.255.0 /24 | Home/small company |
| D | 224-239 | - | Multicast |
| E | 240-255 | - | Reserved |

---

## Public vs Private IP
- Public IP: unique, given by ISP, used to enter internet
- Private IP: used inside LAN only, cannot access internet directly

Private IP ranges:
- Class A: 10.0.0.0 - 10.255.255.255
- Class B: 172.16.0.0 - 172.31.255.255
- Class C: 192.168.0.0 - 192.168.255.255

### NAT (Network Address Translation)
Translates private IP → public IP to reach internet
And public IP → private IP for incoming traffic

---

## Loopback Address
IP: 127.0.0.1
The device talks to itself
Used for: troubleshooting, ping to device locally

---

## IPv4 vs IPv6
- IPv4: 32 bits = 4 billion addresses (not enough anymore)
- IPv6: 128 bits, 8 groups hexadecimal = 2^128 addresses

---

## Subnetting — Why?
Problem: Class B gives 65,000 hosts
Company needs only 3,000 → 62,000 addresses wasted
Solution: Subnetting = divide one large network into smaller subnets

Example:
- Company 1000 employees → Subnet with 1000 IP
- Company 500 employees → Subnet with 500 IP
- Company 3000 employees → Subnet with 3000 IP
Each gets exactly what it needs = no waste

---

## CIDR (Classless Inter-Domain Routing)
Changed from classfull → classless addressing system
Uses prefix length instead of fixed classes

Prefix length:
- Class A = /8
- Class B = /16
- Class C = /24

### How CIDR works
/24 means: 24 bits for network, 8 bits for host
32 - 24 = 8 bits for hosts
2^8 = 256 - 2 = 254 usable addresses

Key rule: always subtract 2
- Network address (first IP)
- Broadcast address (last IP)

Example 192.168.0.0 /24:
- Network: 192.168.0.0
- Broadcast: 192.168.0.255
- Valid hosts: 192.168.0.1 → 192.168.0.254 (254 hosts)

### Changing prefix changes everything
If you change bits for network → network and host counts both change
More network bits = more subnets, fewer hosts per subnet

---

## Bandit Level 2
Challenge: file with spaces in name
Problem: cat "spaces in this filename" needs quotes
Solution: cat "spaces in this filename"
Or: cat spaces\ in\ this\ filename
