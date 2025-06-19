from simulation.datacenter import DataCenter
import time

def benchmark():
    dc = DataCenter()
    for quorum in [(1,1), (2,1), (2,2)]:
        start = time.time()
        dc.simulate_write("key", "value", R=quorum[0], W=quorum[1], N=3)
        latency = time.time() - start
        print(f"R={quorum[0]}, W={quorum[1]}: Latency={latency:.4f}s")

if __name__ == "__main__":
    benchmark()
