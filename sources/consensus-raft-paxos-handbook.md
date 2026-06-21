---
title: "Đồng thuận phân tán (Raft & Paxos) — Data Engineering Handbook"
type: source
source_type: article
author: "Data Engineering Handbook (kythuatdulieu.github.io)"
url: "https://kythuatdulieu.github.io/concepts/1-distributed-systems-architecture/consensus-raft-paxos/"
source_date: 2026-06-15
ingested: 2026-06-21
tags: [distributed-systems, consensus, raft, paxos, distributed-consensus, leader-election]
concepts: [distributed-consensus, leader-election]
---

## Summary

A comprehensive exploration of distributed consensus algorithms — the heart of modern distributed databases and message queues — from the Vietnamese Data Engineering Handbook. Covers the consensus problem's three properties (Agreement, Validity, Termination), the FLP impossibility result, Paxos (Lamport, 1989) as the theoretical foundation, Raft (Ongaro & Ousterhout, 2014) as the human-understandable alternative, and a side-by-side comparison of their trade-offs.

## Core Message

> Consensus algorithms like Raft and Paxos solve the fundamental problem: how does a cluster of servers reach unanimous agreement on data state, even when some servers crash, the network partitions, or messages are delayed? Without consensus, distributed systems risk split-brain — where two cluster halves both claim to be leader and write conflicting data, causing permanent data corruption.

## Key Takeaways

1. **Three consensus properties**: Agreement (all non-faulty nodes agree on the same value), Validity (the agreed value was proposed by a node), Termination (every node eventually decides) — FLP theorem proves no asynchronous algorithm can satisfy all three if even one node fails
2. **Safety over Liveness**: Paxos and Raft both sacrifice Termination (Liveness) when the network is too unstable, prioritizing Agreement and Validity (Safety) — they may temporarily hang rather than risk inconsistency
3. **Paxos** (Lamport, 1989): The first provably correct consensus algorithm. Three roles — Proposers (propose values), Acceptors (vote), Learners (record agreed values). Two-phase protocol (Prepare/Promise → Accept/Accepted). Multi-Paxos chains multiple instances for replicated logs (Google Spanner, Chubby)
4. **Why Paxos is hard**: Basic Paxos only reaches consensus on a single value; building a replicated log requires hand-crafted Multi-Paxos. Lamport's paper is highly abstract, leaving edge cases for engineers to solve
5. **Raft** (2014): Born from the frustration that Paxos is too hard. Decomposes consensus into three independent sub-problems: Leader Election, Log Replication, and Safety. Uses a Strong Leader model with one-way data flow — only the leader handles writes
6. **Leader Election in Raft**: Randomized election timeouts minimize split-vote scenarios. Uses Term numbers to prevent stale leaders from corrupting the log. Heartbeat mechanism (AppendEntries) suppresses unnecessary elections
7. **Ecosystem**: Raft dominates modern infrastructure — etcd (Kubernetes metadata), Consul, CockroachDB, TiDB, Neo4j, Kafka KRaft mode. Paxos powers large-scale systems — Google Spanner, Amazon DynamoDB (lightweight Paxos), Apache Cassandra
8. **Performance trade-off**: Paxos/Multi-Paxos can achieve higher scalability when hand-optimized (no leader bottleneck for proposals), while Raft's single-leader model creates a network bottleneck under extreme write loads

## Companion Concepts

→ [[distributed-consensus]]
→ [[leader-election]]
