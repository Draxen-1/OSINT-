import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
LOG_FILE = os.path.join(OUTPUT_DIR, "results.json")

def log_result(module, target, result):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = {
        "module": module,
        "target": target,
        "result": result
    }

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

