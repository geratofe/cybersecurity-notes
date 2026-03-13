# OSI Model

The **OSI Model (Open Systems Interconnection Model)** is a conceptual framework used to understand how different networking systems communicate over a network.

It divides network communication into **7 layers**, where each layer has a specific function.

---

## OSI Model Layers

| Layer Number | Layer Name | Main Function | Example Protocols and Standards |
|---------------|------------|---------------|--------------------------------|
| Layer 7 | Application Layer | Providing services and interfaces to applications | HTTP, FTP, DNS, POP3, SMTP, IMAP |
| Layer 6 | Presentation Layer | Data encoding, encryption, and compression | Unicode, MIME, JPEG, PNG, MPEG |
| Layer 5 | Session Layer | Establishing, maintaining, and synchronizing sessions | NFS, RPC |
| Layer 4 | Transport Layer | End-to-end communication and data segmentation | TCP, UDP |
| Layer 3 | Network Layer | Logical addressing and routing between networks | IP, ICMP, IPSec |
| Layer 2 | Data Link Layer | Reliable data transfer between adjacent nodes | Ethernet (802.3), WiFi (802.11) |
| Layer 1 | Physical Layer | Physical data transmission media | Electrical, optical, and wireless signals |

---

## Summary

The OSI model helps network engineers, developers, and cybersecurity professionals understand where network problems occur and how data moves through a network.

Each layer performs a specific role and communicates with the layers directly above and below it.

---

## Why It Matters in Cybersecurity

Understanding the OSI model helps identify where attacks or vulnerabilities occur. For example:

- **Layer 7 (Application)** → Web attacks such as SQL injection or XSS  
- **Layer 4 (Transport)** → Port scanning and TCP/UDP attacks  
- **Layer 3 (Network)** → IP spoofing or routing attacks  
- **Layer 2 (Data Link)** → ARP spoofing or MAC attacks
