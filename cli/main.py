import argparse
import random
import time
from simulation.datacenter import DataCenter
from simulation.logger import log_operation, summarize_results


def simulate():
    parser = argparse.ArgumentParser(description="Geo-Distributed Database Simulator")
    parser.add_argument("--ops", type=int, default=20, help="Number of operations")
    parser.add_argument("--fail_rate", type=float, default=0.0, help="Failure rate for nodes (0 to 1)")
    parser.add_argument("--dc", type=int, default=2, help="Number of data centers")
    parser.add_argument("--nodes", type=int, default=2, help="Nodes per data center")
    parser.add_argument("--W", type=int, default=2, help="Write quorum")
    parser.add_argument("--R", type=int, default=2, help="Read quorum")

    args = parser.parse_args()

    dcs = []
    for i in range(args.dc):
        dc = DataCenter(name=f"dc{i+1}", num_nodes=args.nodes, fail_rate=args.fail_rate)
        dcs.append(dc)

    for i in range(args.ops):
        key = f"key{i}"
        value = f"val{i}"
        dc = random.choice(dcs)
        start = time.time()
        success = dc.write_to_quorum(key, value, quorum=args.W)
        latency = (time.time() - start) * 1000
        log_operation("write", key, value, latency, quorum_met=success)

    for i in range(args.ops):
        key = f"key{i}"
        dc = random.choice(dcs)
        start = time.time()
        value, success = dc.read_from_quorum(key, quorum=args.R)
        latency = (time.time() - start) * 1000
        log_operation("read", key, value, latency, quorum_met=success)

    summarize_results()


if __name__ == "__main__":
    simulate()
