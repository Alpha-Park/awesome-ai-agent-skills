---
name: genpark-json-record-dedup
description: Deduplicate a supplied JSON array by explicit top-level identity fields, preserving order and reporting duplicate source indexes. Use for exact record cleanup, not fuzzy identity matching.
---

# JSON record deduplication

Choose identity fields with the user or use their stated keys. Do not infer that similar names, emails or addresses identify the same person. Compare exact JSON values; strings remain case-sensitive, null differs from a missing field, and booleans differ from numbers. Object key order is ignored; array order is significant. The first record wins, even when a later record contains different non-key fields. Report those discarded indexes rather than claiming records were merged.

Run the bundled Python 3.9+ standard-library helper from this skill folder:

```sh
python scripts/dedup.py < input.json > result.json
```

Input: `{"keys":["id"],"records":[{"id":1,"name":"A"},{"id":1,"name":"B"}]}`.
Output contains `records`, zero-based `kept_indexes`, and `duplicates` with `index` and `kept_index`. Missing identity fields fail the entire input. No source file is modified. Use a new output path, never redirect onto the input file. In PowerShell pipe `Get-Content input.json -Raw` to the helper.

Review the duplicate report before replacing any dataset. This reads the whole input into memory; use a streaming/database solution for inputs too large to fit. It is not a distributed lock or exactly-once execution service. License: repository MIT.
