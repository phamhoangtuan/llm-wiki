---
title: "TLS & HTTPS"
type: concept
tags: [security, encryption, networking, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [TLS, HTTPS, Transport Layer Security]
---

HTTPS uses Transport Layer Security (TLS) to encrypt data between client and server. The handshake combines asymmetric and symmetric encryption — leveraging each for what it does best.

## 3-Step TLS Handshake

**1. Negotiation (Handshake)**
- Client sends "Client Hello": supported TLS versions + cipher suites
- Server responds "Server Hello": selects the most secure common option + sends SSL certificate

**2. Asymmetric Encryption**
- Client validates certificate → uses server's public key to encrypt a session key
- Unidirectional encryption for secure secret exchange over untrusted medium
- Only the server (with private key) can decrypt

**3. Symmetric Encryption**
- Session key established → switch to symmetric encryption
- Bidirectional, fast encryption for data transmission
- "So What?" transition: asymmetric is secure but ~1000× slower; symmetric is fast and efficient for long-lived sessions

## Why Both?

| Property | Asymmetric | Symmetric |
|----------|-----------|-----------|
| Speed | Slow (~1000×) | Fast |
| Key Exchange | Secure over untrusted medium | Requires shared secret |
| Direction | Unidirectional (encrypt with public, decrypt with private) | Bidirectional |
| Use | Initial key exchange only | Ongoing session encryption |

TLS combines both: asymmetric for secure key exchange, symmetric for efficient data transmission.

---
- Foundation for [[sso]] — SSO token exchange must occur over TLS
- Foundation for [[password-storage]] — credentials in transit must be encrypted
- Foundation for [[system-design-interview]] — security in transit is a standard design requirement