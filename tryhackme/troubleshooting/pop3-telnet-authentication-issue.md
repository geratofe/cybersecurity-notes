# Troubleshooting: POP3 Authentication Issue with Telnet

## Room

Networking Core Protocols

## Task

Task 7

## Scenario

While completing **Task 7** in the Networking Core Protocols room on TryHackMe, the objective was to interact with an email service running on **port 110** using Telnet.

Port **110** is the default port used by **POP3 (Post Office Protocol v3)**, a protocol responsible for **retrieving emails from a mail server**.

In this task, the POP3 service was running on a mail server powered by **Dovecot**.

## Initial Connection Attempt

I attempted to connect to the service using Telnet:

telnet 10.49.191.237 110

The connection was successful and the server responded:

Trying 10.49.191.237...
Connected to 10.49.191.237.
Escape character is '^]'.
+OK Dovecot (Ubuntu) ready.

This response confirms:

* The server is reachable
* The POP3 service is active
* The server software is Dovecot

## Authentication Attempt

I then attempted to begin authentication using the POP3 command:

AUTH

Server response:

+OK
.

At this point, it became clear that **plain authentication was not allowed over this connection**. The service was refusing plaintext authentication, meaning credentials could not be sent over an unencrypted session.

## Problem

Although the connection to the POP3 service was successful, **Telnet could not be used to authenticate because the server required a secure (TLS/SSL) connection before allowing login**.

Since Telnet only supports **unencrypted TCP communication**, it cannot perform the TLS handshake required by the server.

This prevented authentication using standard POP3 commands such as:

USER username
PASS password

# Workaround: Using OpenSSL to Access POP3 Over TLS

## Problem Recap

The POP3 service running on port **110** refused authentication because plaintext credentials were not allowed on an unencrypted connection.

Since **Telnet cannot establish encrypted connections**, it could not be used to authenticate with the server.

To work around this limitation, a tool capable of creating a **TLS encrypted connection** was required.

---

# Solution: Using OpenSSL

To interact with the POP3 server securely, I used **OpenSSL** to connect to the service over a TLS-enabled port.

Command used:

openssl s_client -connect 10.49.191.237:995

---

# What is OpenSSL

OpenSSL is an **open-source cryptographic toolkit** that provides:

* implementations of encryption algorithms
* TLS/SSL protocol support
* certificate management
* command-line tools for testing secure network services

One of its tools, **s_client**, can act as a TLS client that connects to encrypted services and allows manual interaction with the underlying application protocol.

In penetration testing and network analysis, it is commonly used to:

* test encrypted services
* inspect TLS certificates
* manually communicate with encrypted protocols such as HTTPS, POP3S, IMAPS, and SMTPS.

---

# Explanation of the Command

The command used was:

openssl s_client -connect 10.49.191.237:995

Each part of the command has a specific function.

---

## openssl

This calls the **OpenSSL command-line program**.

It provides access to different cryptographic tools and subcommands.

---

## s_client

`s_client` stands for **SSL/TLS client**.

This mode allows OpenSSL to behave like a client connecting to a server using TLS encryption.

It performs the following actions:

1. Opens a TCP connection to the server
2. Performs the TLS handshake
3. Establishes an encrypted communication channel

Once the secure tunnel is established, the user can manually send application-layer commands (in this case POP3 commands).

---

## -connect

This option specifies **which server and port to connect to**.

Syntax:

-connect <host>:<port>

In this case:

-connect 10.49.191.237:995

This instructs OpenSSL to connect to the server at IP address **10.49.191.237** on port **995**.

---

## 10.49.191.237

This is the **target server's IP address** where the POP3 service is running.

---

## :995

Port **995** is the standard port for **POP3 over TLS (POP3S)**.

Unlike port 110, which provides plaintext POP3, port 995 requires an **encrypted TLS connection from the start**.

Because OpenSSL supports TLS, it can establish this secure connection successfully.

---

# What Happens During the Connection

When the command runs, several steps occur:

1. A TCP connection is opened to the server
2. A TLS handshake is initiated
3. Encryption keys are negotiated
4. A secure communication tunnel is created
5. POP3 commands can then be sent through the encrypted channel

This allows the user to interact with the POP3 server even when encryption is required.

---

# Why the Renegotiation Error Happened

While retrieving an email message using the POP3 command:

RETR 4

the connection produced an error related to **TLS renegotiation**.

TLS renegotiation occurs when a server attempts to **restart or refresh the encryption session** during an active connection.

Older mail servers sometimes perform renegotiation for security or compatibility reasons.

However, modern versions of OpenSSL disable certain renegotiation behaviors because they were previously associated with security vulnerabilities.

When the server attempted to renegotiate the TLS session, OpenSSL rejected the request, producing an error similar to:

SSL routines:can_renegotiate:wrong ssl version

As a result, the TLS layer interrupted the POP3 command, preventing the message from being retrieved.

---

# Summary

Because the POP3 server required encrypted authentication, Telnet could not be used to log in.

Using **OpenSSL's s_client** allowed a TLS connection to be established with the POP3 service on port 995.

Once the encrypted tunnel was created, POP3 commands could be sent manually to interact with the mail server. However, during message retrieval, the server attempted TLS renegotiation, which OpenSSL rejected, causing the connection error.


# Final Solution: Using the `-quiet` Option

## Issue Recap

When connecting to the POP3 service over TLS using:

openssl s_client -connect 10.49.191.237:995

the connection was successfully established and POP3 commands could be issued. However, when attempting to retrieve an email using:

RETR 4

the connection produced a TLS renegotiation error and the message retrieval failed.

This occurred because the OpenSSL client continued printing TLS diagnostic information and handling renegotiation behavior that interfered with the POP3 interaction.

---

# Workaround Using `-quiet`

To resolve this issue, the connection was established using the `-quiet` option:

openssl s_client -connect 10.49.191.237:995 -quiet

This allowed the POP3 commands to be sent and processed correctly without triggering the renegotiation error.

---

# Explanation of the `-quiet` Option

The `-quiet` flag tells **OpenSSL's s_client** to suppress most of the TLS handshake output and debugging information.

Normally, when using `s_client`, OpenSSL prints a large amount of information such as:

* certificate details
* TLS handshake messages
* cipher negotiation
* verification results

This information is useful for debugging TLS connections but is not necessary when the goal is simply to interact with the service protocol.

By enabling `-quiet`, OpenSSL behaves more like a simple network client and allows the user to interact directly with the application protocol (in this case POP3).

---

# Why `-quiet` Fixed the Problem

The `-quiet` option prevents OpenSSL from continuously managing and displaying TLS session information after the handshake completes.

This results in a cleaner communication channel between the client and the POP3 server.

Because the TLS output and extra session management are suppressed, the POP3 commands such as:

USER
PASS
LIST
RETR

can be sent and received without interruption.

As a result, the server does not trigger the renegotiation behavior that previously caused the TLS error, and the email messages can be retrieved successfully.

---

# Final Result

Using the command:

openssl s_client -connect 10.49.191.237:995 -quiet

successfully established a secure TLS connection and allowed POP3 commands to be executed normally. This enabled the retrieval of the email message containing the required information for the task.

---

# Key Takeaway

When interacting manually with encrypted services using OpenSSL, the `-quiet` option can simplify the connection and prevent TLS debugging output from interfering with the application protocol communication.
