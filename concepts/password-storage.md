---
title: "Password Storage"
type: concept
tags: [security, authentication, cryptography, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [password hashing, password salting]
---

Secure password storage requires defending against rainbow table attacks — precomputed lookup tables mapping hashes to plaintext passwords. The defense: salting.

## Why Plain Hashes Fail

❌ **Plain text storage**: Trivially compromised on breach.
❌ **Unsalted hashes**: Vulnerable to rainbow tables — once `hash("password123")` is known, every user with that password is exposed.

## Salting Protocol

**Salt** = unique, randomly generated string appended before hashing. `hash(password + salt)` produces a unique hash for each user, even when passwords are identical.

### Storage Phase
```
salt = generate_random_salt()           # e.g., "a1b2c3d4"
stored_hash = hash(password + salt)
db.save(user_id, salt, stored_hash)     # salt stored in plaintext
```

### Validation Phase
```
def validate_password(user_id, submitted_password):
    salt = db.get_salt(user_id)
    h1 = hash(submitted_password + salt)
    h2 = db.get_stored_hash(user_id)
    return secure_compare(h1, h2)       # constant-time to prevent timing attacks
```

### Why Salt Is Stored in Plaintext

Salt is **not a secret** — it only ensures each hash is unique, neutralizing rainbow table efficacy. The security comes from the hash function's one-way property, not from salt secrecy.

## Key Requirements

- ✅ Use unique salt per user
- ✅ Use constant-time comparison (`secure_compare`) to prevent timing attacks
- ✅ Use slow hash functions (bcrypt, scrypt, Argon2) — not SHA-256 or MD5
- ❌ Never store plaintext passwords
- ❌ Never use unsalted hashes

---
- Foundation for [[sso]] — SSO identity provider must store credentials with salting
- Foundation for [[tls-https]] — passwords must be transmitted over encrypted channels