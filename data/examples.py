def load_example_cases(path="data/examples/example_cases.json"):
    import json
    with open(path, "r") as f:
        examples = json.load(f)
    print(f"Loaded {len(examples)} example cases.")
    return examples
