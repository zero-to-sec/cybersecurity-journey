# Subnetting Design: VLSM for a 3-Department Company

## 1. Scenario

A company has three departments and one network block to work with:

| Department | Hosts needed |
|------------|--------------|
| Department A | 100 |
| Department B | 50 |
| Department C | 20 |

**Given block:** `192.168.10.0/24` (256 addresses)

**Goal:** Design subnets that serve every department with the least possible waste, and leave room to grow.

---

## 2. Method

For each department I followed these steps:

1. Add 2 to the host requirement (network address + broadcast address).
2. Find the smallest power of 2 that covers it (this is the block size).
3. Convert the block size to a prefix: `prefix = 32 - h`, where `2^h = block size`.
4. Allocate the **largest subnet first**, then continue in order, so the blocks stay aligned and do not overlap.

**Formula:** usable hosts = 2^h - 2

---

## 3. Calculations

| Department | Need | Need + 2 | Block size | h | Prefix | Mask | Usable hosts |
|------------|------|----------|------------|---|--------|------|--------------|
| A | 100 | 102 | 128 | 7 | **/25** | 255.255.255.128 | 126 |
| B | 50 | 52 | 64 | 6 | **/26** | 255.255.255.192 | 62 |
| C | 20 | 22 | 32 | 5 | **/27** | 255.255.255.224 | 30 |

---

## 4. Final Allocation

| Department | Subnet | Network | First usable | Last usable | Broadcast |
|------------|--------|---------|--------------|-------------|-----------|
| A (100) | 192.168.10.0/25 | 192.168.10.0 | 192.168.10.1 | 192.168.10.126 | 192.168.10.127 |
| B (50) | 192.168.10.128/26 | 192.168.10.128 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| C (20) | 192.168.10.192/27 | 192.168.10.192 | 192.168.10.193 | 192.168.10.222 | 192.168.10.223 |
| **Free** | 192.168.10.224/27 | 192.168.10.224 | 192.168.10.225 | 192.168.10.254 | 192.168.10.255 |

**Address space used:** 128 + 64 + 32 = 224 of 256 addresses.
**Left free:** `192.168.10.224/27` (32 addresses) for future growth.

---

## 5. Why Each Choice Was Made

### Department A (100 hosts) -> /25
- `/26` gives only 62 usable hosts, which is **not enough** for 100.
- `/25` gives 126 usable hosts, which fits with 26 spare.
- `/24` would work but would use the entire block and leave nothing for B and C.

### Department B (50 hosts) -> /26
- `/27` gives only 30 usable hosts, which is **not enough** for 50.
- `/26` gives 62 usable hosts, which fits with 12 spare.
- `/25` would work but would waste 76 addresses for no benefit.

### Department C (20 hosts) -> /27
- `/28` gives only 14 usable hosts, which is **not enough** for 20.
- `/27` gives 30 usable hosts, which fits with 10 spare.

### Rule behind every decision
> Choose the **smallest** subnet that still fits the hosts. Smaller than that fails; bigger than that wastes addresses.

---

## 6. Why Not an Equal Split?

An equal split (same prefix for every department) fails in this scenario:

| Option | Result |
|--------|--------|
| Three equal `/25` subnets | A `/24` only contains **2** subnets of `/25`, so a third does not fit. |
| Four equal `/26` subnets | Each has only 62 usable hosts, so Department A (100) **does not fit**. |

Because the departments have very different sizes, the design needs **VLSM (Variable Length Subnet Masking)**: a different prefix length per subnet, sized to the real need.

---

## 7. Waste Analysis

| Department | Usable hosts | Needed | Spare |
|------------|--------------|--------|-------|
| A | 126 | 100 | 26 |
| B | 62 | 50 | 12 |
| C | 30 | 20 | 10 |

The spare addresses inside each subnet are a deliberate growth buffer. In addition, a whole `/27` remains unallocated.

---

## 8. Design Notes

- **Largest first:** allocating A, then B, then C keeps every block aligned on its boundary (0, 128, 192), so no subnets overlap.
- **Growth:** Department C can expand into the free `/27` only if needed, and only by re-planning, so reserve it deliberately.
- **Security benefit:** each department sits in its own broadcast domain, so traffic between departments can be filtered at a router or firewall (for example, an ACL that blocks A from reaching C).

---

## 9. Conclusion

| Department | Subnet | Usable hosts |
|------------|--------|--------------|
| A | 192.168.10.0/25 | 126 |
| B | 192.168.10.128/26 | 62 |
| C | 192.168.10.192/27 | 30 |
| Free | 192.168.10.224/27 | 30 |

All three departments are served, address waste is minimal, and one `/27` is still available for the future.
