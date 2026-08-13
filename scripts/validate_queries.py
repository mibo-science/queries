#!/usr/bin/env python3
"""Validate the MIBO Pilot query artifacts using only the Python standard library."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_FILES = ("v0.1.json", "v0.1.0.json")
INSTRUMENT_FILE = "v0.1.1.json"
HASHES_FILE = "HASHES.json"
EXPECTED_INSTRUMENT_HASH = (
    "8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35"
)
EXPECTED_TEXTS = {
    "q001": "おすすめのプロジェクト管理ツールは？",
    "q002": "What is the best CRM for small businesses?",
    "q003": "睡眠の質を上げる方法を教えて",
    "q004": "How do I implement RAG with a vector database?",
    "q005": "日本の代表的なAI研究者を5人挙げて",
}


def load_json(filename: str) -> Any:
    with (ROOT / filename).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    for filename in HISTORICAL_FILES:
        load_json(filename)

    instrument = load_json(INSTRUMENT_FILE)
    hashes = load_json(HASHES_FILE)

    queries = instrument.get("queries")
    require(isinstance(queries, list), "v0.1.1.json: queries must be a list")
    require(instrument.get("query_count") == 5, "v0.1.1.json: query_count must be 5")
    require(len(queries) == 5, "v0.1.1.json: exactly five queries are required")

    query_ids = [query.get("id") for query in queries]
    require(len(query_ids) == len(set(query_ids)), "v0.1.1.json: query IDs must be unique")
    require(query_ids == list(EXPECTED_TEXTS), "v0.1.1.json: query IDs or order changed")

    require(hashes.get("query_set_version") == "0.1.1", "HASHES.json: wrong query_set_version")
    require(hashes.get("applies_to_file") == INSTRUMENT_FILE, "HASHES.json: wrong applies_to_file")
    hash_queries = hashes.get("queries")
    require(isinstance(hash_queries, dict), "HASHES.json: queries must be an object")
    require(set(hash_queries) == set(query_ids), "HASHES.json: query IDs differ from v0.1.1.json")

    rows: list[str] = []
    for query in queries:
        query_id = query["id"]
        text = query.get("text")
        require(text == EXPECTED_TEXTS[query_id], f"{query_id}: exact query wording changed")

        digest = sha256_text(text)
        require(query.get("exact_text_sha256") == digest, f"{query_id}: embedded text hash mismatch")
        require(hash_queries[query_id].get("text") == text, f"{query_id}: HASHES.json text mismatch")
        require(
            hash_queries[query_id].get("exact_text_sha256") == digest,
            f"{query_id}: HASHES.json digest mismatch",
        )
        rows.append(
            f"{query_id}\t{query['language']}\t{query['category']}\t{text}\n"
        )

    instrument_hash = sha256_text("".join(rows))
    require(instrument_hash == EXPECTED_INSTRUMENT_HASH, "ordered instrument hash changed")
    require(
        instrument.get("instrument_content_sha256") == instrument_hash,
        "v0.1.1.json: instrument hash mismatch",
    )
    require(
        hashes.get("instrument_content_sha256") == instrument_hash,
        "HASHES.json: instrument hash mismatch",
    )

    parsed = ", ".join((*HISTORICAL_FILES, INSTRUMENT_FILE, HASHES_FILE))
    print(f"PASS: parsed {parsed}")
    print("PASS: q001-q005 IDs, exact texts, and UTF-8 SHA-256 digests")
    print(f"PASS: ordered instrument SHA-256 {instrument_hash}")
    print("PASS: HASHES.json is consistent with v0.1.1.json")


if __name__ == "__main__":
    main()
