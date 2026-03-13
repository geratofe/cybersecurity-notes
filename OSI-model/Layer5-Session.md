# OSI Layer 5: Session Layer

The **Session Layer** is the fifth layer of the OSI model. Its main role is to **establish, manage, and terminate sessions** (connections) between applications on different devices.

---

## Main Responsibilities

- **Session establishment, maintenance, and termination**  
- **Synchronization**: Adding checkpoints in long data transfers to resume after interruptions  
- **Dialog control**: Determining whether communication is half-duplex or full-duplex  
- **Managing multiple sessions** between applications

---

## Examples of Session Layer Protocols

| Function | Protocol | Notes |
|----------|---------|-------|
| Remote procedure calls | RPC | Allows programs to execute code on remote systems |
| Network file sharing | NFS | Provides session management for file access over the network |
| Windows sessions | SMB | Manages sessions for file and printer sharing |
| Dialog management | NetBIOS | Session services for legacy systems |

---

## Common Concepts

- **Sessions**: Logical connections between two applications for ongoing communication  
- **Checkpoints / Recovery points**: Helps resume sessions after interruptions  
- **Dialog control**: Determines communication direction and flow  

---

## Why It Matters in Cybersecurity

- **Session hijacking**: Attackers can take over an active session if security is weak  
- **Man-in-the-middle attacks**: Intercepting session traffic  
- **Authentication management**: Ensuring sessions are established with valid credentials  
- **Session timeout policies**: Limiting exposure to attacks

---

## Summary

The Session Layer ensures that communication between applications is **organized, synchronized, and recoverable**. Understanding this layer helps with troubleshooting multi-step network interactions and securing sessions against hijacking or interception.
