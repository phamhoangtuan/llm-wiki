---
title: "Single Sign-On (SSO)"
type: concept
tags: [security, authentication, identity, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [SSO]
---

Single Sign-On allows users to navigate multiple service domains (e.g., Gmail, YouTube, Drive) with a single set of credentials. It neutralizes "password fatigue" — reducing attack surface while increasing user retention.

## 4-Step SSO Workflow

**1. Initial Interception**: User accesses Domain 1 (e.g., Gmail) → unauthenticated → redirected to SSO Server.

**2. Global Session Establishment**: User submits credentials → SSO validates → creates global session + unique token.

**3. Token Handover & Validation**: SSO redirects user back to Domain 1 with token → Domain 1 validates token with SSO → grants access.

**4. Cross-Domain Propagation**: User accesses Domain 2 (e.g., YouTube) → unauthenticated → queries SSO → global session already active → SSO issues new token for Domain 2 → no re-authentication needed.

## Strategic Benefits

- Reduces "password fatigue" — users remember one credential
- Centralizes authentication logic — security policy applied consistently
- Decreases attack surface — fewer credentials to protect
- Improves user retention — seamless cross-product experience

---
- Foundation for [[password-storage]] — SSO still requires secure credential storage at the identity provider
- Foundation for [[tls-https]] — SSO token exchange must occur over encrypted channels