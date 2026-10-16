# Networking Summary: IP Classes, Subnetting, Public/Private IP, NAT

## 1. IP Classes

| Class | First Octet | Default Prefix | Hosts/Network |
|---|---|---|---|
| A | 1 – 126 | /8 | 16,777,214 |
| B | 128 – 191 | /16 | 65,534 |
| C | 192 – 223 | /24 | 254 |

- D (224–239) = Multicast | E (240–255) = Reserved
- `127.0.0.0/8` = Loopback | `169.254.0.0/16` = APIPA (no DHCP)
- Classful is old; today we use CIDR (any prefix).

## 2. Public vs Private IP

- **Public:** globally unique, routable on the Internet (given by ISP).
- **Private:** internal only, not routable, reused by everyone.

| Class | Private Range |
|---|---|
| A | 10.0.0.0/8 |
| B | 172.16.0.0/12 (172.16 – 172.31) |
| C | 192.168.0.0/16 |

## 3. Subnetting

| Prefix | Mask | Block | Hosts |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | .128 | 128 | 126 |
| /26 | .192 | 64 | 62 |
| /27 | .224 | 32 | 30 |
| /28 | .240 | 16 | 14 |
| /29 | .248 | 8 | 6 |
| /30 | .252 | 4 | 2 |

```
Block Size   = 256 − mask value
Usable Hosts = 2^(host bits) − 2
Network      = (IP ÷ Block) rounded down × Block
Broadcast    = Network + Block − 1
Hosts        = Network+1 → Broadcast−1
```

**Example:** `172.16.45.130/26` → Block 64 → 130÷64 = 2 → 2×64 = 128
Network `172.16.45.128` | Broadcast `172.16.45.191` | Hosts `.129 – .190`

**VLSM:** sort largest to smallest, give each the smallest block that fits (hosts + 2), each starts at the previous Broadcast + 1.
`192.168.50.0/24` → A (100) /25 `.0` | B (50) /26 `.128` | C (20) /27 `.192` | P2P /30 `.224`

**Summarization:** count common bits from the left in binary.
`10.1.0.0/24 … 10.1.3.0/24` → `10.1.0.0/22`
Rule: networks count = power of 2, and first network = multiple of the group size.

## 4. NAT

Translates Private IPs to Public IPs when leaving to the Internet (saves IPv4, hides internal network).

| Type | Idea |
|---|---|
| Static | 1 Private ↔ 1 Public (server reachable from outside) |
| Dynamic | Private IPs ↔ pool of Public IPs |
| PAT | Many Private ↔ 1 Public, separated by Port (most common) |

```
192.168.1.10:51000 → 203.0.113.5:40001 → Server:443
192.168.1.11:51000 → 203.0.113.5:40002 → Server:443
```
The router keeps a NAT Table to return replies to the right device.

- NAT is not a Firewall.
