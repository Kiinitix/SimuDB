# SimuDB: A Geo-Distributed Database Simulator

SimuDB is a command-line simulator built with Python, Rust, and C++ to model how geo-distributed databases behave under different consistency models, quorum settings, and node failures.

It allows you to:
1. Simulate multiple datacenters and nodes
2. Control replication (W) and read quorum (R)
3. Inject node failures at custom rates
4. Observe the effects of replication strategy in real-time

---

## Why SimuDB?

Distributed databases like Cassandra, DynamoDB, and Spanner use quorum-based replication to balance availability and consistency. SimuDB makes it easy to understand these trade-offs by letting you experiment in a safe, local sandbox.

---

## Installation (via Docker)

### 1. Clone the repository

```bash
git clone https://github.com/kiinitix/simudb.git
cd simudb
```

### 2. Build the Docker image

```
docker build -t simudb .
```

### 3. Run the simulator

```
docker run --rm simudb --ops 50 --fail_rate 0.1
```

### You can customize:

    --ops – number of operations to simulate

    --fail_rate – failure rate per node (0.0 to 1.0)

    --nodes – number of nodes per data center

    --dc – number of data centers

    --W – write quorum

    --R – read quorum

### Example:

```
docker run --rm simudb --dc 2 --nodes 3 --W 2 --R 2 --ops 100 --fail_rate 0.2
```

### Example Output

```
[Node 0 @ dc1] Stored foo -> bar
[Node 1 @ dc1] Stored foo -> bar
-> Written with quorum W=2
-> Read value: bar
```
