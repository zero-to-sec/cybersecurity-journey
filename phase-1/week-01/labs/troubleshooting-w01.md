# Troubleshooting Challenge - Week 1

**Date:** 2026-10-27
**Target:** 192.168.56.101 (my own VirtualBox VM, Host-Only network)
**Goal:** Diagnose an unexpected scan result instead of accepting the first result.

## 1. Observe

I scanned port 8000 from Windows:

```
nmap -p 8000 192.168.56.101
```

```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 14:38 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0010s latency).

PORT     STATE    SERVICE
8000/tcp filtered http-alt
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.47 seconds
```

The port is `filtered`, not `open` or `closed`.

## 2. Hypothesize

1. **Firewall:** the packets are blocked and there is no response at all.
2. **Port closed:** there is no service listening on it.

## 3. Test

**Test 1:** I ran `sudo ufw status` to check if a firewall is active.

```
Status: active

To                         Action      From
--                         ------      ----
8000/tcp                   DENY        Anywhere
8000/tcp (v6)              DENY        Anywhere (v6)
```

This confirms hypothesis 1.

**Test 2:** I ran `ss -tlnp | grep 8000` to check if anyone is listening.

```
(no output)
```

There is no output, so nothing is listening on port 8000. This also confirms hypothesis 2.

Both hypotheses are true at the same time. They do not exclude each other.

## 4. Diagnose

There are **two** causes: an active firewall AND a stopped server. At first I only saw the firewall effect, because the firewall hid the second problem.

## 5. Fix

### Fix 1: Disable the firewall

```
sudo ufw disable
```

```
Firewall stopped and disabled on system startup
```

**Verify:** I scanned again from Windows.

```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 15:27 +0000
Nmap scan report for 192.168.56.101
Host is up (0.0010s latency).

PORT     STATE  SERVICE
8000/tcp closed http-alt
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.23 seconds
```

**Conclusion:** The firewall was causing `filtered`, but the fix revealed another problem: the port is `closed` because no server is running.

### Fix 2: Restart the server

I restarted the server in a separate terminal:

```
python -m http.server 8000
```

**Verify (inside the VM):**

```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Verify (from Windows):**

```
Starting Nmap 7.992 ( https://nmap.org ) at 2026-10-27 15:33 +0000
Nmap scan report for 192.168.56.101
Host is up (0.00s latency).

PORT     STATE SERVICE
8000/tcp open  http-alt
MAC Address: 08:00:27:8A:35:D2 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 1.21 seconds
```

**Conclusion:** The second cause was that the server was not running.

## 6. Explain Why

Two problems were hidden behind a single result. The firewall was concealing the fact that the server was down, which only became apparent after the firewall was removed.

This also explains the difference between the two states:
- **filtered:** no response, because the firewall drops the packets.
- **closed:** a `reset` response, because the VM itself rejects the connection.

**Security note:** I used `ufw disable`, which turns off the whole firewall and opens all ports. In a real environment, it is better to delete only the specific rule:

```
sudo ufw delete deny 8000/tcp
```
