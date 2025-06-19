import random
import time
from simulation.node import Node

class Node:
    def __init__(self, node_id, dc_name=None, fail_rate=0.0):
        self.node_id = node_id
        self.dc_name = dc_name
        self.fail_rate = fail_rate
        self.store_data = {}

    def store(self, key, value):
        if random.random() < self.fail_rate:
            print(f"[Node {self.node_id} @ {self.dc_name}] Write failed due to simulated failure")
            return False
        self.store_data[key] = value
        print(f"[Node {self.node_id} @ {self.dc_name}] Stored {key} -> {value}")
        return True

    def retrieve(self, key):
        if random.random() < self.fail_rate:
            print(f"[Node {self.node_id} @ {self.dc_name}] Read failed due to simulated failure")
            return None
        value = self.store_data.get(key)
        if value is not None:
            print(f"[Node {self.node_id} @ {self.dc_name}] Retrieved {key} -> {value}")
        return value


class DataCenter:
    def __init__(self, name, num_nodes, fail_rate=0.0):
        self.name = name
        self.nodes = [Node(node_id=i, dc_name=name, fail_rate=fail_rate) for i in range(num_nodes)]

    def write_to_quorum(self, key, value, quorum):
        successes = 0
        for node in self.nodes:
            if node.store(key, value):
                successes += 1
            if successes >= quorum:
                print(f"-> Written with quorum W={quorum}")
                return True
        print(f"-> Write failed to meet quorum W={quorum}")
        return False

    def read_from_quorum(self, key, quorum):
        values = []
        for node in self.nodes:
            value = node.retrieve(key)
            if value is not None:
                values.append(value)
            if len(values) >= quorum:
                print(f"-> Read value: {values[0]}")
                return values[0], True
        print(f"-> Read failed to meet quorum R={quorum}")
        return None, False
