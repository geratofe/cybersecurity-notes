# OSI Layer 2: Data Link Layer

The **Data Link Layer** is the second layer of the OSI model. Its main role is to provide **reliable data transfer between two directly connected nodes** and to handle errors that occur at the physical layer.

---

## Main Responsibilities

- Dividing the raw bit stream into **frames**
- Detecting and sometimes correcting **errors** in transmitted frames
- Controlling **flow of data** between devices on the same network
- Managing **physical addressing** (MAC addresses)
- Providing **access control** for shared media (like WiFi or Ethernet)

---

## Examples of Data Link Layer Standards

| Function | Example Standards | Notes |
|----------|-----------------|-------|
| Wired LAN | Ethernet (802.3) | Most common local network standard |
| Wireless LAN | WiFi (802.11) | Wireless networks, handles media access and MAC addresses |
| WAN | PPP, HDLC | Point-to-Point Protocol and High-Level Data Link Control |
| Error detection | CRC, Parity | Ensures data integrity in frames |

---

## Common Concepts

- **Frames**: Packages of data including headers, payload, and error-checking info.
- **MAC Addresses**: Unique hardware addresses used to identify devices on a LAN.
- **Flow Control**: Prevents a fast sender from overwhelming a slow receiver.
- **Switches**: Operate at Layer 2 to forward frames based on MAC addresses.

---

## Why It Matters in Cybersecurity

- **MAC spoofing attacks**: Attackers can change their MAC address to impersonate another device.
- **ARP spoofing/poisoning**: Intercepting traffic on the local network.
- **Network segmentation**: Understanding VLANs and how data is isolated at Layer 2.
- **Frame sniffing**: Capturing raw frames for analysis (e.g., using Wireshark).

---

## Summary

The Data Link Layer ensures that the raw bits from the physical layer are **packaged, addressed, and error-checked** so they can be reliably delivered to the next device. Mastery of this layer is essential for network troubleshooting and securing local networks.
