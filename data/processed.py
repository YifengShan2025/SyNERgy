def preprocess_data(raw_data):
    # Placeholder preprocessing logic
    processed_data = []
    for item in raw_data:
        # Apply tokenization, cleaning, or filtering here
        processed_data.append(item)  # Dummy step
    return processed_data

def save_processed_data(data, path="data/processed/processed_data.json"):
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved processed data to {path}")
