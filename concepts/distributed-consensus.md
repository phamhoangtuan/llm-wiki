---
title: "Distributed Consensus (Raft & Paxos)"
type: concept
tags: [distributed-systems, consensus, raft, paxos, fault-tolerance, distributed-consensus]
created: 2026-06-21
updated: 2026-06-21
sources: [consensus-raft-paxos-handbook]
aliases: [Consensus Algorithm, Raft, Paxos, Multi-Paxos, Đồng thuận phân tán]
---

**Distributed consensus** is the process by which multiple nodes in a network reach unanimous agreement on a value or sequence of actions, even when some nodes fail, the network partitions, or messages are delayed (source: [[consensus-raft-paxos-handbook]]).

These algorithms are the heart of modern distributed databases and message queues — [[Apache Kafka]], Zookeeper, etcd, MongoDB, and Cassandra all depend on consensus for data integrity. Without it, systems risk **split-brain**: two cluster halves both claiming to be leader, writing conflicting data, causing permanent corruption.

## The Consensus Problem

A correct consensus algorithm must satisfy three properties:

1. **Agreement**: All non-faulty nodes must agree on the same value
2. **Validity**: The agreed value must have been proposed by some node in the system (not garbage)
3. **Termination**: Every non-faulty node eventually reaches a decision (no infinite hanging)

### FLP Impossibility

The **FLP theorem** (Fischer, Lynch, Paterson, 1985) proved that in a fully asynchronous network with even one faulty node, no deterministic consensus algorithm can guarantee all three properties simultaneously. This means Paxos and Raft must make a trade-off: they guarantee **Safety** (Agreement + Validity) and sacrifice **Liveness** (Termination) — they may temporarily hang if the network is too unstable, but they will never return a wrong answer.

### Safety vs Liveness

| | Safety | Liveness |
|---|---|---|
| **Guarantee** | Nothing bad happens | Something good eventually happens |
| **In practice** | No two nodes decide differently | System eventually makes progress |
| **Violation** | Split-brain, data corruption | Temporarily unavailable, hanging |
| **Priority in Paxos/Raft** | **Absolute priority** | Best-effort; sacrificed during severe partitions |

## Paxos: The Theoretical Foundation

Introduced by Leslie Lamport in 1989, Paxos was the first consensus algorithm proven mathematically safe in unreliable networks (fail-stop model).

### Roles

A node can serve multiple roles simultaneously:
- **Proposer**: Proposes a value for consensus
- **Acceptor**: Votes on proposed values (the "voting body")
- **Learner**: Records and persists the agreed-upon value

### Two-Phase Protocol

**Phase 1 — Prepare/Promise**:
1. Proposer generates a Proposal ID higher than any previous ID
2. Sends `Prepare(ID)` to a majority of Acceptors
3. If ID > any ID the Acceptor has seen, it replies `Promise` — pledging to reject any proposal with a lower ID

**Phase 2 — Accept/Accepted**:
4. Once Proposer receives majority `Promise` responses, it sends `Accept(ID, Value)`
5. Acceptors record the value and notify Learners

### Multi-Paxos

Basic Paxos only reaches consensus on a single value. To build a replicated log suitable for state machine replication, multiple Paxos instances are chained into **Multi-Paxos** — electing a stable leader to reduce the message complexity from two phases to one (Phase 2 only, since Prepare is skipped when the leader is stable).

**Systems using Paxos/Multi-Paxos**: Google Spanner, Google Chubby, Amazon DynamoDB (lightweight Paxos), Apache Cassandra (lightweight transactions).

### Why Paxos is Difficult to Implement

Lamport's original paper (*The Part-Time Parliament*) is famously abstract, using a fictional Greek parliament metaphor. *Paxos Made Simple* (2001) clarified the algorithm, but the gap between theory and production code remains vast: edge cases around leader changes, log compaction, membership changes, and performance optimization are not specified by the protocol itself. Most production Paxos deployments are heavily custom-engineered by organizations with deep distributed systems expertise.

## Raft: Designed for Human Understanding

Diego Ongaro and John Ousterhout (Stanford, 2014) created Raft in response to Paxos's notorious complexity, with the explicit goal: **understandability** — while maintaining equivalent safety guarantees.

### Decomposition

Raft breaks the consensus problem into three independent sub-problems:

1. **Leader Election**: Select one server to exclusively handle write requests
2. **Log Replication**: Leader synchronizes its log to all Followers
3. **Safety**: Ensure no two leaders can overwrite each other's committed entries

### State Machine

```
[Start] → Follower
Follower → Candidate : Election timeout (no heartbeat)
Candidate → Leader : Wins majority vote
Candidate → Follower : Discovers leader with higher Term
Leader → Follower : Discovers leader with higher Term
```

Every Raft node exists in one of three states: Follower (passive, responds to leaders), Candidate (actively seeking election), or Leader (handles all client requests). Term numbers monotonically increase — a higher Term always supersedes a lower one.

### Leader Election

All nodes start as Followers. If a Follower receives no heartbeat (AppendEntries RPC) from the Leader within a **randomized election timeout** (150-300ms), it transitions to Candidate, increments its Term, votes for itself, and sends `RequestVote` to all other nodes.

- **Majority wins**: Candidate becomes Leader if it receives votes from a majority of nodes
- **Split vote**: If two Candidates emerge simultaneously and neither gets a majority, both timeout, increment Term, and retry. Randomized timeouts make repeated splits exponentially unlikely
- **Term enforcement**: If a node receives an RPC from a leader with a higher Term, it steps down

### Log Replication

Client writes flow through the Leader:

1. Leader appends the command to its local log (uncommitted)
2. Leader sends `AppendEntries` RPCs to all Followers (also serves as heartbeat)
3. Once the entry is replicated to a **majority** of nodes, the Leader commits it
4. Leader applies the committed entry to its state machine and returns success to the client
5. Followers learn of new commit index on the next `AppendEntries` and apply committed entries

**Critical safety property**: A Leader can never overwrite committed entries. When a new Leader is elected, it must contain all committed entries from previous Terms — Raft enforces this through the election restriction (a Candidate cannot win unless its log is at least as up-to-date as the majority).

### One-Way Data Flow

Unlike Paxos where any node can propose, Raft has **strict one-way flow**: data travels only from Leader → Followers. Followers never redirect clients or propose values. This simplifies reasoning about the system state at the cost of making the Leader a potential bottleneck.

## Raft vs Paxos: Comparison

| Criterion | Paxos / Multi-Paxos | Raft |
|---|---|---|
| **Understandability** | Extremely complex; often custom-engineered by FAANG-scale orgs | Highly intuitive; standardized libraries across all major languages |
| **Leader model** | Peer-to-peer or single leader (Multi-Paxos); any node can propose | Strong Leader only; only the Leader handles client writes |
| **Data flow** | Multi-directional; nodes negotiate independently | One-way: Leader → Followers |
| **Performance** | Very high when hand-optimized; less leader bottleneck | Leader can become network bottleneck under extreme write load |
| **Edge cases** | Many unspecified; implementers must discover and handle | Explicitly enumerated and handled in the paper itself |
| **Membership changes** | Not defined in core protocol; ad-hoc extensions | Built-in joint consensus mechanism for safe reconfiguration |

## Ecosystem

- **Raft**: etcd (Kubernetes metadata store), Consul (HashiCorp service mesh), CockroachDB, TiDB, Neo4j, Apache Kafka (KRaft mode — replacing Zookeeper), YugabyteDB
- **Paxos**: Google Spanner (globally distributed SQL), Google Chubby (distributed lock service), Amazon DynamoDB (lightweight Paxos for leader election), Apache Cassandra (lightweight transactions)

---

## Connections

- [[byzantine-fault-tolerance]] — BFT extends consensus to adversarial node behavior (lying, corruption); Raft/Paxos are CFT algorithms that assume fail-stop (nodes simply crash, don't lie). BFT requires `3f+1` nodes vs `2f+1` for CFT
- [[cap-theorem]] — Consensus algorithms are the mechanism that enables CP systems; without consensus, distributed stores must choose between consistency and availability during partitions
- [[leader-election]] — Leader election is the first sub-problem Raft decomposes; randomized timeouts and Term numbers ensure at most one leader per Term
- [[apache-kafka]] — Kafka's KRaft mode replaces Zookeeper with a self-managed Raft-based metadata quorum (KIP-500)
- [[database-replication]] — Consensus underlies master election in replication clusters; ensures a single writable primary
- [[scalable-architecture]] — Consensus is required for coordination services (locks, config, leader election) that enable horizontal scaling
