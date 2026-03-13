# OSI Layer 1: Physical Layer

The **Physical Layer** is the first layer of the OSI model. It is responsible for **the actual transmission of raw data bits over a physical medium**. This layer defines the hardware, electrical, optical, or wireless specifications needed to send and receive signals.

---

## Main Responsibilities

- Transmitting **raw binary data** (0s and 1s) across the network
- Defining **cabling, connectors, and physical topologies**
- Setting **signal types, voltages, and timing**
- Handling **bit rate and synchronization**
- Supporting **multiplexing techniques** for sending multiple signals simultaneously

---

## Examples of Physical Layer Standards

| Medium Type | Example Standard | Notes |
|------------|----------------|-------|
| Copper cabling | Ethernet (10BASE-T, 100BASE-TX) | Twisted pair copper cabling, most common LAN medium |
| Fiber optics | 1000BASE-LX, 10GBASE-SR | High-speed, long-distance optical communication |
| Wireless | WiFi (802.11a/b/g/n/ac/ax), Bluetooth | Radio frequency or infrared signals |
| Electrical signals | RS-232, RS-485 | Serial communication for devices |

---

## Common Concepts

- **Bit transmission**: Sending raw 1s and 0s as electrical, optical, or radio signals.
- **Duplex modes**: Half-duplex vs full-duplex communication.
- **Signal encoding**: Techniques like Manchester encoding or NRZ (Non-Return-to-Zero).
- **Physical topologies**: Star, bus, ring, mesh — define how devices are physically connected.

---

## Why It Matters in Cybersecurity

Even though Layer 1 doesn’t handle software or protocols directly, security at the physical layer is critical:

- Protecting **cabling and devices** from tampering
- Preventing **unauthorized physical access** to network equipment
- Avoiding **signal interception** (e.g., tapping copper lines or intercepting WiFi signals)
- Ensuring **redundancy and fault tolerance** for critical infrastructure

---

## Summary

The Physical Layer is the foundation of all networking. Without a solid physical connection and correct signaling, higher-level protocols cannot function. Understanding this layer helps cybersecurity professionals ensure network integrity and prevent physical attacks.
