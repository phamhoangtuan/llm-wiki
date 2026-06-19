---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, consistency, availability, architecture, database-design]
created: 2026-06-17
updated: 2026-06-17
sources: [cap-theorem-handbook]
aliases: [Brewer's Theorem, Định lý CAP, CAP]
---

**CAP Theorem** (also known as Brewer's Theorem) states that any distributed data store can provide at most two of three guarantees simultaneously: **Consistency**, **Availability**, and **Partition Tolerance** (source: [[cap-theorem-handbook]]).

Formulated by Eric Brewer in 2000 and formally proven by Seth Gilbert and Nancy Lynch (MIT) in 2002, CAP is the most important architectural constraint in distributed system design.

## The Three Properties

### C — Consistency
Every read receives the most recent write (or an error). All nodes in the distributed system see the same data at the same time. A strongly consistent system behaves as if it were a single machine — even though it's a cluster.

### A — Availability
Every request (read or write) receives a non-error response — even if some nodes are down or unreachable. The response may not contain the latest data.

### P — Partition Tolerance
The system continues to operate despite arbitrary message loss or network failures between nodes. The network is allowed to drop, delay, or reorder messages between nodes.

## Why P is Non-Negotiable

In any real distributed system — cloud (AWS, GCP, Azure) or on-premise — network partitions **will** happen. Causes include:
- Switch/router failures
- Packet loss due to congestion
- GC pauses that break heartbeat timeouts
- Undersea cable cuts
- DDoS attacks saturating links

Since P cannot be opted out of, the real architectural choice is **CP** (Consistency + Partition Tolerance) or **AP** (Availability + Partition Tolerance). The theoretical **CA** system can only exist on a single-node database (e.g., a standalone PostgreSQL instance) — not in a distributed setting.

## CAP-C vs ACID-C: A Critical Distinction

A common confusion: the "C" in CAP is **not** the "C" in ACID.

| | CAP Consistency | ACID Consistency |
|---|---|---|
| **Scope** | Distributed system level | Single database transaction level |
| **Meaning** | All replicas show identical data | Data satisfies all constraints (FK, UNIQUE, triggers) |
| **Violation** | Client reads stale data from a lagging replica | Invalid data written that violates schema rules |
| **Example** | Async master-slave: slave returns outdated row | Bank transfer: total money unchanged before/after |

A system can be ACID-compliant (all constraints enforced) while being CAP-inconsistent (reads from a lagging replica return stale data).

## CP Architecture: Consistency Over Availability

When a network partition occurs, CP systems **reject requests** on the minority partition rather than risk serving stale data. The system prefers returning `500` or `Timeout` errors over returning inconsistent results.

**Representative systems**: Google Bigtable, Apache HBase, MongoDB (with `w: "majority"`), Zookeeper, etcd, CockroachDB.

**Data Engineering use cases**:
- Core banking ledgers and financial transactions
- Inventory management (preventing double-selling)
- Metadata stores (Hive Metastore)
- Reconciliation services

### MongoDB CP Example
```javascript
db.transactions.insertOne(
  { transaction_id: "TXN12345", amount: 5000, status: "COMPLETED" },
  { writeConcern: { w: "majority", wtimeout: 5000 } }
);
// If > half the nodes are unreachable, this times out with an error
// Consistency is preserved; availability is sacrificed
```

## AP Architecture: Availability Over Consistency

During partitions, AP systems **continue serving requests** on all reachable nodes, accepting that data may be temporarily inconsistent. They rely on **Eventual Consistency** — background anti-entropy mechanisms reconcile diverged copies once the network heals.

**Representative systems**: Amazon DynamoDB, Apache Cassandra, CouchDB, Riak.

**Data Engineering use cases**:
- User-facing applications (profile updates, shopping carts)
- CDN edge caches
- Social media feeds
- IoT sensor data ingestion

### Cassandra AP Example
```cql
CONSISTENCY ONE;
SELECT * FROM user_profiles WHERE user_id = 'U123';
// Returns immediately from any replica — may be stale
// Trade-off: low latency for potentially outdated data
```

### Consistency Models in AP Systems

AP systems offer tunable consistency levels:
- **Eventual Consistency**: Replicas converge over time with no guarantees on when
- **Causal Consistency**: Operations with causal relationships are seen in order
- **Read-Your-Writes**: A client always sees its own writes
- **Monotonic Reads**: A client never sees older data than it previously saw

## Quorum: Bridging CP and AP

Quorum-based systems allow per-operation tuning between consistency and availability. The key formula:

- `N` = total replication factor
- `R` = number of replicas that must acknowledge a read
- `W` = number of replicas that must acknowledge a write

**Strong consistency**: `R + W > N` — read and write quorums overlap, guaranteeing at least one node has the latest data.

**Eventual consistency**: `R + W ≤ N` — no guaranteed overlap, higher availability, potential for stale reads.

**Example** (Cassandra, N=3):
- `QUORUM` (R=2, W=2): R+W = 4 > 3 → strong consistency
- `ONE` (R=1, W=1): R+W = 2 ≤ 3 → eventual consistency

## Split-Brain and Quorum Resolution

**Split-brain** occurs when a network partition divides a cluster into two subgroups that both believe they are the majority and continue accepting writes independently — creating irreconcilable data divergence.

**Solution**: Majority quorum (`N/2 + 1`). A partition can only operate if it controls more than half the nodes. The minority partition refuses writes. Zookeeper, etcd, and most consensus systems embed this principle.

## PACELC: CAP's Evolution

**PACELC Theorem** (Abadi, 2012) refines CAP by distinguishing behavior during partitions vs normal operation:

| Condition | Trade-off |
|---|---|
| **P**artition | **A**vailability vs **C**onsistency |
| **E**lse (no partition) | **L**atency vs **C**onsistency |

Modern systems map to PACELC categories:
- **PC/EC** (Cassandra): Prefer consistency during partition; eventual consistency in normal ops
- **PA/EL** (DynamoDB): Prefer availability during partition; favor latency in normal ops
- **PC/EC** (MongoDB): Prefer consistency during partition; eventual consistency in normal ops (default reads from primary)

## Best Practices for Data Engineers

1. **Start with AP for user-facing services** — latency matters more than perfect consistency for most apps
2. **Use CP for financial/audit data** — incorrect data is worse than slow data
3. **Tune quorum, not architecture** — modern databases (Cassandra, MongoDB) let you set consistency per-operation; don't change the entire architecture for edge cases
4. **Understand your failure mode** — what happens when the network breaks? Define the degraded experience explicitly
5. **Don't optimize for P before measuring** — many teams over-engineer for partitions that happen rarely; measure actual network reliability first
6. **PACELC informs normal-operation choices** — even without partitions, there's a latency-vs-consistency trade-off every day

---

## Connections

- [[byzantine-fault-tolerance]] — BFT extends fault tolerance beyond crash-stop to arbitrary (Byzantine) failures; CAP only models crash-stop and network partitions
- [[database-replication]] — Master-slave replication is the mechanism that creates the C-vs-A tension in CAP
- [[scalable-architecture]] — CAP is the fundamental constraint on how distributed data stores scale
- [[message-queue]] — Async messaging decouples producers/consumers, trading consistency for availability — an AP pattern
- [[cache-strategy]] — Caches are inherently AP: they optimize for latency/availability over consistency
