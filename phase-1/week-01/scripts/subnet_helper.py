# subnet_helper.py: My First Security Script (Week 1)

> Goal: turn my manual subnetting method into a Python script.
> Rule: built with Week 1 tools only (`input`, `split`, indexing, `int`, variables, f-strings, math).
> Environment: Kali Linux (VirtualBox), Python 3, Mousepad.

## What the script does

It reads an IP/CIDR from the user (example: `192.168.1.130/26`) and prints:
Mask, Network, Broadcast, Usable range, and number of Hosts.

Script: [`scripts/subnet_helper.py`](../scripts/subnet_helper.py)

Run it:

```bash
python3 subnet_helper.py
```

## My manual method (from my notebook)

1. Block size = 2 ** (32 - cidr)
2. Mask (last octet) = 256 - block size
3. Network = (last octet // block size) * block size
4. Broadcast = Network + block size - 1
5. Usable = Network + 1 to Broadcast - 1
6. Hosts = block size - 2

## How each manual step became code

| Manual step | Python |
|---|---|
| Split IP and prefix | `ip_adress.split("/")` |
| Get each octet | `ip.split(".")` then `octets[0]`, `octets[3]`... |
| Text to number | `int(parts[1])` and `int(octets[3])` |
| Block size | `block = 2 ** hosts_bits` |
| How many blocks fit | `n = last // block` |
| Network | `network = n * block` |
| Broadcast | `broadcast = network + block - 1` |
| Mask | `mask = 256 - block` |
| Print result | f-strings |

## Test results (run in Kali)

| Input | Mask | Network | Broadcast | Usable | Hosts |
|---|---|---|---|---|---|
| `192.168.1.130/26` | 255.255.255.192 | 192.168.1.128 | 192.168.1.191 | 192.168.1.129 to 192.168.1.190 | 62 |
| `10.0.0.77/30` | 255.255.255.252 | 10.0.0.76 | 10.0.0.79 | 10.0.0.77 to 10.0.0.78 | 2 |
| `192.168.1.200/27` | 255.255.255.224 | 192.168.1.192 | 192.168.1.223 | 192.168.1.193 to 192.168.1.222 | 30 |
| `172.20.5.9/24` | 255.255.255.0 | 172.20.5.0 | 172.20.5.255 | 172.20.5.1 to 172.20.5.254 | 254 |

All four results match my manual calculation.

Screenshot from Kali:

![subnet_helper.py running on 4 examples in Kali](../assets/subnetting-by-python.png)

## Bugs I hit and how I fixed them

| Bug | Cause | Fix |
|---|---|---|
| `dict(input(...))` for the IP | `input()` returns a string, and `dict()` needs key-value pairs | one `input()`, then `split()` |
| `cidr = 26` written again after extracting it | it overwrote the real value (a silent bug) | removed the fixed line |
| `parts[1] - 24` | `parts[1]` is text, not a number | `cidr = int(parts[1])` |
| `T = one % block` | `%` gives the remainder, not "how many blocks". It worked for 130 by luck | `n = last // block` |
| `192.186.1` instead of `192.168.1` | typo in a fixed text | the octets now come from the input |
| `Cidr` vs `cidr` | Python is case sensitive, so they are two names | one consistent lowercase name |

## How I built it

First I wrote a version that followed my notebook step by step. It worked for my example but used fixed numbers. Then I studied how to get every value from the input, and rebuilt the final version using only Week 1 tools.

## Limits (honest)

- Works for prefixes `/24` to `/30` only, because the split happens in the last octet.
- `/31` and `/32` give wrong results (no usable range).
- Prefixes smaller than `/24` (like `/20`) need the third octet, so they need `if` and functions.
- No input validation yet (a wrong IP will crash the script).

## What I understood (in my own words)

I learned how to turn a manual method into code. My notebook method is: find the block size, divide the last octet by it, then multiply back. In Python I use `//` for the division, not `%`, because `%` gives the remainder. `split()` cuts text into a list, and `parts[0]` is the first item because counting starts from 0. I use `int()` only on the values I calculate with (`cidr` and `last`), and I keep the other octets as text because I only print them.

## Evidence

- [x] Script runs in Kali on 4 different examples
- [x] Screenshot added
- [x] Results match my manual calculation
- [ ] Teach-Back done (explained without notes)

## Next step (Week 2)

Version 2: support any prefix (`/0` to `/32`) using `if`/`else` and functions, and validate the input.
