# Nmap - Complete Notes

## What is Nmap?
Nmap (Network Mapper) is used for:
- Host discovery
- Port scanning
- Service detection
- OS fingerprinting
- Network enumeration

---

## Core Concepts
- Host → target machine  
- Port → entry point to a service  
- State → open / closed / filtered  
- Service → software running on a port  

---

## Basic Scan
```bash
nmap <target>
```
Scans top 1000 TCP ports.

---

## Host Discovery

```bash
nmap -sn <target>
```
- Ping scan  
- Checks if host is alive (no port scan)

```bash
nmap -Pn <target>
```
- Skips ping  
- Treats host as up  

---

## Port Scanning

```bash
nmap -p <ports> <target>
```

Examples:
```bash
nmap -p 22,80,443 <target>
nmap -p 1-1000 <target>
```

```bash
nmap -p- <target>
```
- Scans all 65535 ports  

```bash
nmap -F <target>
```
- Fast scan (top 100 ports)  

---

## Scan Types

```bash
nmap -sS <target>
```
- SYN scan (stealth)  
- Fast, less detectable  

```bash
nmap -sT <target>
```
- Full TCP connect scan  

```bash
nmap -sU <target>
```
- UDP scan (slow, important)  

---

## Service & Version Detection

```bash
nmap -sV <target>
```
- Detects service versions  

---

## OS Detection

```bash
nmap -O <target>
```

---

## Script Scanning

```bash
nmap -sC <target>
```
- Runs default scripts  

---

## Aggressive Scan

```bash
nmap -A <target>
```

Includes:
- OS detection  
- Version detection  
- Scripts  
- Traceroute  

---

## Timing

```bash
-T0 to -T5
```

- T0 → very slow (stealth)  
- T4 → fast (recommended)  
- T5 → very fast (noisy)  

Example:
```bash
nmap -T4 <target>
```

---

## Output Options

```bash
nmap -oN output.txt <target>
```
- Normal output  

```bash
nmap -oX output.xml <target>
```
- XML format  

```bash
nmap -oG output.gnmap <target>
```
- Greppable format  

---

## Useful Flags

```bash
nmap -v <target>
```
- Verbose  

```bash
nmap -vv <target>
```
- More verbose  

```bash
nmap --reason <target>
```
- Shows why a port is in a state  

```bash
nmap -sL <target>
```
- List targets only (no scan)  

---

## Most Useful Combinations

### Initial Recon (MOST IMPORTANT)
```bash
nmap -sC -sV -T4 <target>
```

### Full Scan (Deep Recon)
```bash
nmap -p- -sC -sV -T4 <target>
```

### Stealth Scan
```bash
nmap -sS -T2 <target>
```

### Quick Scan
```bash
nmap -F <target>
```

### No Ping Scan
```bash
nmap -Pn <target>
```

### UDP + TCP Scan
```bash
nmap -sS -sU -T4 <target>
```

### Aggressive Scan
```bash
nmap -A <target>
```

---

## Workflow (Best Practice)

1. Initial scan:
```bash
nmap -sC -sV -T4 <target>
```

2. Full scan:
```bash
nmap -p- -T4 <target>
```

3. Targeted scan:
```bash
nmap -sC -sV -p <open ports> <target>
```

---

## Summary

- `-sS` → stealth scan  
- `-sV` → version detection  
- `-O` → OS detection  
- `-p-` → all ports  
- `-sC` → scripts  
- `-T4` → speed  
- `-Pn` → skip ping  

---

## Notes

- Always have permission before scanning  
- Nmap is a core reconnaissance tool  
- Combine with:
  - Wireshark  
  - Netcat  
  - Burp Suite  
