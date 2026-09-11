---
title: "Database Isolation Levels"
type: concept
tags: [databases, transactions, concurrency, system-design]
created: 2026-06-21
updated: 2026-06-21
sources: [system-design-big-archive]
aliases: [ACID isolation, transaction isolation]
---

Database isolation allows transactions to execute as if no other concurrent transactions exist. Guaranteed by MVCC (Multi-Version Concurrency Control) and locks.

## Four Isolation Levels

| Level | Description | Example | Use When |
|-------|-------------|---------|----------|
| Serializable 🔒 | Highest level; transactions execute sequentially as if one at a time | Banking transfers where order matters | Financial systems, critical consistency |
| Repeatable Read 🔄 | Reads consistent with transaction start point | User profile reads during session | Most OLTP applications |
| Read Committed ✅ | Data modifications visible only after commit | E-commerce product views | Default for PostgreSQL, Oracle |
| Read Uncommitted ⚠️ | Allows "dirty reads" — uncommitted modifications visible | Analytics dashboards (tolerate stale data) | Rarely used in production |

Higher isolation = stronger consistency but lower concurrency. Each level is a trade-off.

## Optimistic Locking

When conflicts are rare and retry cost is lower than lock overhead, use optimistic concurrency control with version numbers:

```
class Product:
    def update_price(self, new_price, current_version):
        product = db.get_product(self.id)
        if product.version != current_version:
            raise ConcurrentModificationError("Data changed, retry")
        product.price = new_price
        product.version += 1
        db.save(product)
```

Check version before update, retry on conflict. Best for scenarios like e-commerce cart updates where simultaneous edits are uncommon.

---
- Foundation for [[database-sharding]] — isolation guarantees must hold across shards
- Contrast with [[cap-theorem]] — isolation is Consistency in ACID, which CAP treats differently
- Related to [[database-replication]] — isolation levels affect read consistency across replicas