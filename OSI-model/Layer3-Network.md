# OSI Layer 3: Network Layer

The **Network Layer** is the third layer of the OSI model. Its main responsibility is **logical addressing, routing, and forwarding data across different networks**.

---

## Main Responsibilities

- **Logical addressing** (e.g., IP addresses)
- **Routing** packets from source to destination across multiple networks
- Fragmenting and reassembling packets if necessary
- Handling **congestion control** in some protocols

---

## Examples of Network Layer Protocols

| Function | Protocol | Notes |
|----------|---------|-------|
| Logical addressing | IP (IPv4, IPv6) | Assigns unique addresses to devices |
| Routing | ICMP | Internet Control Message Protocol for error and diagnostic messages |
| Security | IPSec | Provides network-layer encryption and authentication |
| Routing protocols | OSPF, BGP | Determine the best path for packets across networks |

---

## Common Concepts

- **Packets**: Units of data at Layer 3, containing source and destination IP addresses.
- **Routing tables**: Maps used by routers to determine packet paths.
- **Subnetting**: Dividing networks into smaller logical segments.
- **TTL (Time to Live)**: Prevents packets from circulating endlessly in a network loop.

---

## Why It Matters in Cybersecurity

- **IP spoofing attacks**: Attacker sends packets with a forged source IP.
- **Routing attacks**: Manipulating routing tables to intercept or redirect traffic.
- **Packet sniffing**: Capturing and analyzing network packets.
- **Network segmentation & firewall rules**: Layer 3 knowledge is key to isolating networks and controlling traffic flow.

---

## Summary

The Network Layer ensures that data can travel **from one device to another across networks**, even if they are separated by multiple hops. Understanding Layer 3 is critical for network design, routing, and security.
