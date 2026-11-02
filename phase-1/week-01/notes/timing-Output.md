### Timing Templates (`-T0` to `-T5`)

| Template | Name | Speed | Typical Use |
|----------|------|-------|-------------|
| `-T0` | Paranoid | Extremely slow (~5 min between probes) | IDS evasion |
| `-T1` | Sneaky | Very slow (~15 sec between probes) | IDS evasion |
| `-T2` | Polite | Slow (~0.4 sec between probes) | Low bandwidth / less load on target |
| `-T3` | Normal | Default | General scanning |
| `-T4` | Aggressive | Fast | Fast, reliable networks (common in CTFs/labs) |
| `-T5` | Insane | Fastest | Very fast networks; may miss open ports |

### Output Formats

| Option | Format | Description | Best For |
|--------|--------|-------------|----------|
| `-oN file` | Normal | Human-readable, same as terminal output | Reading / reports |
| `-oX file` | XML | Structured data | Tools & parsing (Metasploit, scripts) |
| `-oG file` | Grepable | One line per host (deprecated) | Quick `grep`/`awk` filtering |
| `-oA base` | All | Saves all three formats at once | Keeping full results |

**Example:**
```bash
nmap -sT -sV -T4 -oA scan_results 192.168.1.10
```
