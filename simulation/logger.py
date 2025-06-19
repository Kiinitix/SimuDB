import csv
import os
from datetime import datetime

LOG_FILE = "output/simulation_log.csv"


def log_operation(op_type, key, value, latency_ms, quorum_met):
    os.makedirs("output", exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["timestamp", "op_type", "key", "value", "latency_ms", "quorum_met"])
        writer.writerow([
            datetime.now().isoformat(),
            op_type,
            key,
            value,
            latency_ms,
            quorum_met
        ])


def summarize_results():
    print("\n Simulation complete. Log stored at:", LOG_FILE)
