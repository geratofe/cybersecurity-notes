# OSI Layer 6: Presentation Layer

The **Presentation Layer** is the sixth layer of the OSI model. Its main role is to **translate, encrypt, and compress data** so that it can be properly interpreted by the application layer.

---

## Main Responsibilities

- **Data translation/formatting**: Converts data between different formats (e.g., from EBCDIC to ASCII)  
- **Encryption and decryption**: Ensures secure communication  
- **Compression and decompression**: Reduces data size for faster transmission  

---

## Examples of Presentation Layer Standards

| Function | Standard / Protocol | Notes |
|----------|------------------|-------|
| Data encoding | Unicode, ASCII | Converts data into a standard format for applications |
| File formats | JPEG, PNG, MPEG | Ensures multimedia files are correctly interpreted |
| Encryption | SSL/TLS | Encrypts data for secure communication |
| Data serialization | XML, JSON | Standardizes structured data for transmission |

---

## Common Concepts

- **Encoding/decoding**: Ensures data can be read and understood by the receiving system  
- **Encryption**: Protects sensitive information during transit  
- **Compression**: Reduces bandwidth usage and speeds up transmission  

---

## Why It Matters in Cybersecurity

- **Secure communications**: Encryption (SSL/TLS) prevents eavesdropping  
- **Data integrity**: Proper encoding prevents misinterpretation or corruption  
- **Attack prevention**: Understanding presentation layer functions can help identify weaknesses in encryption or compression implementations

---

## Summary

The Presentation Layer makes sure that data is **formatted, encrypted, and compressed** correctly before it reaches the application layer. Mastery of this layer is important for secure communications and handling multimedia or structured data.
