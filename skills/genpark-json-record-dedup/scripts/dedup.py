"""Exact JSON-key deduplication, preserving first occurrences. MIT."""
import json
import sys


def deduplicate(data):
    keys, records = data.get("keys"), data.get("records")
    if not isinstance(keys, list) or not keys or any(not isinstance(k, str) for k in keys):
        raise ValueError("keys must be a non-empty list of strings")
    if len(set(keys)) != len(keys) or not isinstance(records, list):
        raise ValueError("keys must be unique and records must be an array")
    seen, kept, indexes, duplicates = {}, [], [], []
    for index, record in enumerate(records):
        if not isinstance(record, dict) or any(k not in record for k in keys):
            raise ValueError(f"record {index} is not an object or has missing identity fields")
        identity = json.dumps([record[k] for k in keys], sort_keys=True, ensure_ascii=False, allow_nan=False)
        if identity in seen:
            duplicates.append({"index": index, "kept_index": seen[identity]})
        else:
            seen[identity] = index
            kept.append(record)
            indexes.append(index)
    return {"records": kept, "kept_indexes": indexes, "duplicates": duplicates}


if __name__ == "__main__":
    sys.stdin.reconfigure(encoding="utf-8-sig")
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        data = json.load(sys.stdin)
        if not isinstance(data, dict):
            raise ValueError("input must be an object")
        print(json.dumps(deduplicate(data), ensure_ascii=False, allow_nan=False))
    except (ValueError, TypeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
