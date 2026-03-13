# OSI Layer 4: Transport Layer

The **Transport Layer** is the fourth layer of the OSI model. Its main responsibility is **end-to-end communication between devices**, ensuring that data is delivered **completely and in order**.

---

## Main Responsibilities

- **Segmentation and reassembly**: Splitting large messages into smaller segments and reassembling them at the destination.
- **End-to-end connection management**: Establishing, maintaining, and terminating connections.
- **Flow control**: Preventing the sender from overwhelming the receiver.
- **Error detection and correction**: Ensuring reliable delivery.

---

## Examples of Transport Layer Protocols

| Protocol | Type | Notes |
|----------|------|-------|
| TCP | Connection-oriented | Reliable, ordered, error-checked delivery of data |
| UDP | Connectionless | Fast, but no guarantee of delivery or order |
| SCTP | Connection-oriented | Supports multiple streams and reliability, often used in telecom |

---

## Common Concepts

- **Ports**: Logical endpoints used to identify applications (e.g., port 80 for HTTP, port 22 for SSH).
- **Segmentation**: Dividing data into smaller pieces for transmission.
- **Acknowledgements (ACKs)**: Confirming receipt of data (used in TCP).
- **Windowing**: Technique for flow control and efficient data transfer.

---

## Why It Matters in Cybersecurity

- **Port scanning**: Attackers often scan for open TCP/UDP ports to identify services.
- **TCP attacks**: SYN floods, session hijacking, and man-in-the-middle attacks.
- **UDP attacks**: Amplification attacks (e.g., DNS amplification).
- **Reliable delivery**: Ensuring critical data (like credentials or financial info) is delivered correctly.

---

## Summary

The Transport Layer ensures that data sent from one application on a device reaches the correct application on another device **accurately and reliably**. Understanding Layer 4 is crucial for troubleshooting, network analysis, and security monitoring.
