# DNS & HTTP - Week 1 Notes

## DNS (Domain Name System)
Translates domain names → IP addresses
Like a phone book for the internet

### DNS Hierarchy
1. Root Name Server → knows all TLD servers
2. TLD Server (.com, .org) → knows domain info
3. Authoritative Name Server → gives final IP

### How DNS Works
1. You type google.com
2. OS checks cache first
3. Asks DNS Resolver (ISP)
4. Resolver asks Root Server → TLD → Authoritative
5. Gets IP → connects to website

### Kali Commands
nslookup google.com     → query DNS for IP
dig google.com          → detailed DNS info
dig google.com +short   → IP only
curl -I https://google.com → show HTTP headers

---

## HTTP & HTTPS
HTTP  = Hypertext Transfer Protocol (port 80)
HTTPS = HTTP + TLS encryption (port 443)
Client sends Request → Server sends Response

### HTTP Methods
GET    → get data from server
POST   → send data to server
PUT    → update existing data
DELETE → delete data

### HTTP Request contains
- Method + URL
- Headers
- Body (for POST/PUT)

### HTTP Response Status Codes
200 = OK (success)
300 = Redirect
400 = Bad Request
401 = Unauthorized
403 = Not Permission (Forbidden)
404 = Not Found
500 = Problem in Server

### HTTP vs HTTPS
HTTP  → port 80, not encrypted
HTTPS → port 443, TLS encrypted
Request goes through TLS handshake first

---

## DHCP (Dynamic Host Configuration Protocol)
Automatically assigns IP to devices
Gives: IP, Subnet Mask, Default Gateway, DNS Server, Lease Time

### DNS vs DHCP
DNS  = translates names to IPs
DHCP = assigns IP to your device automatically

### Kali Commands
curl -I http://example.com   → HTTP headers (port 80)
curl -I https://example.com  → HTTPS headers (port 443)
### Kali Commands
curl -I http://example.com   → HTTP headers (port 80)
curl -I https://example.com  → HTTPS headers (port 443)
