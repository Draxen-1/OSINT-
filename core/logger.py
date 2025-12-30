import json
from datetime import datetime

LOG_FILE = "output/results.json"

def log_result(module, target, data):
    entry = {
        "time": str(datetime.utcnow()),
        "module": module,
        "target": target,
        "result": data
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
