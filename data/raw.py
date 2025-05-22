import os
import json

def load_raw_data(directory="data/raw"):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as f:
                data.append(json.load(f))
    print(f"Loaded {len(data)} raw files.")
    return data
