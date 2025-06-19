import random
import time

class Network:
    def __init__(self, latency_ms=100, drop_rate=0.0):
        self.latency_ms = latency_ms
        self.drop_rate = drop_rate

    def send(self, msg):
        if random.random() < self.drop_rate:
            print("[✖] Packet dropped")
            return None
        time.sleep(self.latency_ms / 1000.0)
        return msg
