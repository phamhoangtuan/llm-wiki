---
title: "Leader Election"
type: concept
tags: [distributed-systems, consensus, raft, fault-tolerance, coordination]
created: 2026-06-21
updated: 2026-06-21
sources: [consensus-raft-paxos-handbook]
aliases: [Bầu chọn Leader, Leader Election Algorithm]
---

**Leader Election** is the process by which a distributed system selects a single node to act as the coordinator — exclusively handling writes, assigning work, or maintaining cluster state — ensuring that even if the current leader fails, a new one is quickly and safely elected (source: [[sources/consensus-raft-paxos-handbook]]).

Leader election is a fundamental building block of distributed consensus: both [[distributed-consensus|Raft]] and Multi-Paxos rely on it to simplify coordination by funneling all decisions through a single node. Systems like [[apache-kafka|Apache Kafka]], Zookeeper, etcd, and MongoDB all embed leader election mechanisms.

## Why Leaders?

Without a leader, distributed systems face two pathologies:
- **Split-brain**: Two nodes both believe they're in charge, accepting conflicting writes → permanent data corruption
- **Coordination chaos**: Multi-writer protocols (some Paxos variants) have O(N²) communication complexity for every decision

A strong leader reduces distributed consensus to a simpler problem: only one node makes decisions, and consensus becomes "make sure followers agree the leader is still the leader."

## Leader Election in Raft

Raft's leader election is the canonical example — designed to be simple, safe, and fast. Every node in a Raft cluster exists in one of three states: **Follower**, **Candidate**, or **Leader**.

### The Election Trigger

All nodes start as Followers. A Follower expects regular **heartbeats** (AppendEntries RPCs) from the Leader. If it receives no heartbeat within a **randomized election timeout** (typically 150-300ms), it assumes the Leader has failed and triggers an election.

### Election Process

1. **Follower → Candidate**: The node increments its current **Term** (a monotonically increasing integer), votes for itself, and sends `RequestVote` RPCs to all other nodes
2. **Voting rule**: Each node grants its vote to at most one Candidate per Term. It votes for the first Candidate whose log is at least as up-to-date as its own (log completeness guarantee)
3. **Majority wins**: The Candidate becomes Leader if it receives votes from a **majority** of nodes (`N/2 + 1`). It immediately begins sending heartbeats to assert authority and suppress new elections
4. **Split vote**: If two Candidates emerge simultaneously and neither gets a majority (each gets exactly `N/2`), both timeout, increment Term, and retry

### Randomized Timeouts: The Key Insight

If every Follower had the same election timeout, split votes would be inevitable — every node would become a Candidate at the same instant. **Randomized timeouts** (e.g., 150-300ms uniform random) make it overwhelmingly probable that one node times out first, becomes Candidate, and wins the election before others even start.

The winner's timeout expires first; it declares candidacy and receives votes before competitors even begin their campaigns.

### Term-Based Safety

The **Term** number is Raft's logical clock. Rules:
- A node always defers to a higher Term: Follower → Candidate → Leader
- If a Leader discovers a higher Term (from another node's RPC), it immediately steps down to Follower
- Stale leaders (network-partitioned from a previous Term) cannot corrupt the log because Followers reject their requests with outdated Terms

This prevents the classic split-brain scenario where an isolated former leader continues accepting writes.

## Leader Election in Multi-Paxos

Multi-Paxos also uses a leader to reduce message complexity (from two phases to one), but the election mechanism is less explicitly defined than Raft's. Paxos allows any node to become leader simply by issuing `Prepare` with a higher Proposal ID — an implicit election embedded in the consensus protocol itself rather than a separate sub-protocol.

## Coordination Services

Several production systems provide ready-made leader election:

| System | Mechanism | Used By |
|---|---|---|
| **Zookeeper** | Ephemeral sequential znodes; lowest sequence number wins | Apache Kafka (legacy), Hadoop, HBase |
| **etcd** | Raft consensus; leader elected via Raft's built-in mechanism | Kubernetes (cluster state) |
| **Consul** | Raft-based; integrated with health checking and service discovery | Nomad, Vault, service mesh |
| **Apache Kafka KRaft** | Raft-based metadata quorum (KIP-500) | Kafka 3.3+ (replaces Zookeeper) |

## Common Failure Modes

- **Flaming leader**: Leader is alive but too slow — followers time out and elect a new one, causing constant churn. Mitigation: increase election timeout, add leader load shedding
- **Network partition**: Leader isolated on minority partition — cannot get majority for writes, but may still believe it's leader until it contacts a quorum and discovers a higher Term
- **Zombie leader**: Former leader on minority partition keeps processing reads from cached data — solved by leases (time-bounded leadership) or requiring quorum for reads

---

## Connections

- [[distributed-consensus]] — Raft decomposes consensus into Leader Election as its first sub-problem; Paxos embeds leader election implicitly in the Prepare phase
- [[byzantine-fault-tolerance]] — BFT leader election requires additional safeguards since Byzantine nodes may lie about being leader; PBFT also uses a leader-based model
- [[cap-theorem]] — Leader election via majority quorum (`N/2 + 1`) is the mechanism that prevents split-brain, a CAP-critical failure mode
- [[apache-kafka]] — Kafka brokers use Zookeeper (legacy) or KRaft (Raft-based) for controller election; partition leaders are elected per-topic-partition
- [[database-replication]] — Master-slave replication depends on electing a single writable primary; leader election failures cause replication stalls
