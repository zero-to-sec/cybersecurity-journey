Ip addr  
#lo 
1. LOOPBACK,UP,LOWER_UP: the interface is working
2. mtu: maximum packet size that can be sent
3. link/loopback: don't have MAC address
4. inet: ip address IPV4 local host
5. inet6: IPV6
6. valid_lft forever: permanent Ip address

#eth0
1. BROADCAST,MULTICAST: network streaming is supported
2. qdisc fq_codel: packets sorting algorithm
3. state up: online and worked
4. link/ether: NIV Mac address
5. brd: broadcast mac address
6. inet: my Ip address
7. brd: broadcast adrdess
8. scope global: suitable for offline communication
9. dynamic: it takes automatic by DHCP
10. valid_lft 84938sec: valid to 24 hours


IP route
[DESTINATION] [via the gate] [dev NIC] [proto source] [scope] [src my address] [metric]


Ping
1. 56(84): Data size + headers
2. icmp_seq=1: packet sequence num
3. ttl=64: time to live
4. time: latency, time of round trip
5. rtt: time of departure and return
6. min/avg/max/mdev: fast answer/average/slower answer/connection stability


nslookup
1. Server: my router
2. Address: port of DNS
3. Non-authoritative: unreliable answer


dig
#Header
1. opcode: QUERY: operation type - regular query
2. status: NOERROR: successful query without error
3. id: number that links the question to the answer

#flags
1. qr rd ra: Query response - recursion desired - recursion available
2. authority: official server
3. additional: additional record

#OPT PSEUDOSECTION
1. good: it protects against (sppofing)

#ANSWER SECTION
1. 227: the time in seconds the answer is saved in tha cache, after which it is asked again
2. Query time: response time
