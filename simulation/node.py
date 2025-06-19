class Node:
    def __init__(self, node_id, dc_name):
        self.id = node_id
        self.dc = dc_name
        self.store = {}  # key -> (value, timestamp)

    def write(self, key, value, timestamp):
        self.store[key] = (value, timestamp)
        print(f"[Node {self.id} @ {self.dc}] Stored {key} -> {value}")

    def read(self, key):
        return self.store.get(key, None)
