# OSI Model - Week 1 Notes

## Layer 1 - Physical
#Responsible for: cable type, voltage, signal format, transmission speed, connector type, wire arrangement and converting 0-1 to an actual signal
الكابل الفعلي
This layer deals with: How bits will actually move within the real word
Problem in this Layer are often a cut cable - a faulty port - a weak signal - or a damaged NIC
Example: Ethernet cable, Wi-Fi signal

## Layer 2 - Data Link
4 functions: Framing, MAC Address, Media Access, Error Detection
MAC = physical device identity, 48 bits
CSMA/CD = collision detection (Old Ethernet)
CSMA/CA = collision prevention (Wi-Fi)
Error Detection & Correction: Parity check, Check Sum, CRC 
Example: Network card
Transmission modes: Simplex, Half-duplex, Full-duplex
Example: Internet, Talkie-walkie

## Layer 3 - Network
Logical addressing - IP Address عنوان الجهاز على الشبكة
Routing: find best, shortest path between networks
Protocols: RIP, OSPF (Routing protocols)
Data unit: Packet
Example: Router
Example: 192.168.1.1
Commands: ip addr, ping

## Layer 4 - Transport
Breaks data into Segments
Sends data from Sender to Receiver
TCP = connection-based, guarantees delivery - يضمن وصول البيانات
UDP = fast, no guarantee - سريع بدون ضمان
Data unit: Segment
Example: TCP for web browsing, UDP for video calls

## Layer 5 - Session
Opens, manages, and closes sessions between devices
فتح وإغلاق الاتصال بين جهازين
1 functions: Session Management
Example: You were watching a Youtube video and suddenly the internet cut out for a few seconds and then come back
Example 2: When the internet goes down on Facebook, it retains the posts that were uploaded
Example 3: Login session on Facebook - staying logged in

## Layer 6 - Presentation
Encryption/Decryption
تشفير وتحويل البيانات
Example: old SSL/new TLS encryption
Translation between formats
Data Compression
Example: Uploading photo to Facebook (compression 122kb → smaller)

## Layer 7 - Application
Where users interact with the network
Protocols: HTTP, FTP, SMTP, DNS
Ex: HTTP → browsing, FTP → download/upload files
Ex: SMTP → sending emails
Example: Opening google.com automatically uses HTTPS protocol
Commands: curl -I https://google.com
Authentication, Authorization
